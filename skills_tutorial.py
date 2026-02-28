"""
技能扩展教程
详细演示如何为 LangChain 代理添加新的技能（工具）
"""
import os
import json
from datetime import datetime
from typing import List, Dict, Optional
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


# ============================================================
# 第一部分：简单技能 - 直接定义函数
# ============================================================

def get_stock_price(stock_code: str) -> str:
    """查询股票价格（模拟）
    
    Args:
        stock_code: 股票代码，如 AAPL, TSLA, 00700
    
    Returns:
        股票价格信息
    """
    # 模拟数据
    mock_data = {
        "AAPL": "苹果 (AAPL): $175.23 ↑ +2.3%",
        "TSLA": "特斯拉 (TSLA): $242.56 ↓ -1.2%",
        "00700": "腾讯 (00700.HK): HK$368.20 ↑ +0.8%",
        "MSFT": "微软 (MSFT): $378.91 ↑ +1.5%",
    }
    return mock_data.get(stock_code.upper(), f"{stock_code} 股票数据暂时无法获取")


def send_email(to: str, subject: str, content: str) -> str:
    """发送邮件（模拟）
    
    Args:
        to: 收件人邮箱
        subject: 邮件主题
        content: 邮件内容
    
    Returns:
        发送结果
    """
    # 实际应用中这里可以调用真实的邮件服务
    return f"✉️ 邮件已发送\n收件人: {to}\n主题: {subject}\n内容: {content[:50]}..."


def create_reminder(task: str, time: str) -> str:
    """创建提醒事项
    
    Args:
        task: 提醒内容
        time: 提醒时间
    
    Returns:
        创建结果
    """
    return f"⏰ 提醒已创建\n任务: {task}\n时间: {time}\n将在指定时间通知您！"


# ============================================================
# 第二部分：带状态的技能 - 使用类封装
# ============================================================

class NotebookSkill:
    """笔记本技能 - 记录和管理笔记"""
    
    def __init__(self):
        self.notes: Dict[str, str] = {}
    
    def add_note(self, title: str, content: str) -> str:
        """添加笔记
        
        Args:
            title: 笔记标题
            content: 笔记内容
        """
        self.notes[title] = content
        return f"📝 笔记已保存: {title}"
    
    def get_note(self, title: str) -> str:
        """获取笔记
        
        Args:
            title: 笔记标题
        """
        if title in self.notes:
            return f"📖 {title}:\n{self.notes[title]}"
        return f"❌ 未找到笔记: {title}"
    
    def list_notes(self) -> str:
        """列出所有笔记"""
        if not self.notes:
            return "📂 笔记本是空的"
        notes_list = "\n".join([f"- {title}" for title in self.notes.keys()])
        return f"📚 笔记列表:\n{notes_list}"


class TaskManagerSkill:
    """任务管理技能"""
    
    def __init__(self):
        self.tasks: List[Dict] = []
    
    def add_task(self, task: str, priority: str = "normal") -> str:
        """添加任务
        
        Args:
            task: 任务描述
            priority: 优先级 (high/normal/low)
        """
        task_id = len(self.tasks) + 1
        self.tasks.append({
            "id": task_id,
            "task": task,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        emoji = "🔴" if priority == "high" else "🟡" if priority == "normal" else "🟢"
        return f"{emoji} 任务已添加 (#{task_id}): {task}"
    
    def complete_task(self, task_id: int) -> str:
        """完成任务
        
        Args:
            task_id: 任务ID
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                return f"✅ 任务已完成: {task['task']}"
        return f"❌ 未找到任务 #{task_id}"
    
    def list_tasks(self, status: Optional[str] = None) -> str:
        """列出任务
        
        Args:
            status: 筛选状态 (pending/completed/all)
        """
        if not self.tasks:
            return "📋 任务列表为空"
        
        filtered_tasks = self.tasks
        if status == "pending":
            filtered_tasks = [t for t in self.tasks if t["status"] == "pending"]
        elif status == "completed":
            filtered_tasks = [t for t in self.tasks if t["status"] == "completed"]
        
        result = "📋 任务列表:\n"
        for task in filtered_tasks:
            status_emoji = "✅" if task["status"] == "completed" else "⏳"
            priority_emoji = "🔴" if task["priority"] == "high" else "🟡" if task["priority"] == "normal" else "🟢"
            result += f"{status_emoji} {priority_emoji} #{task['id']} {task['task']}\n"
        
        return result


# ============================================================
# 第三部分：外部 API 集成技能
# ============================================================

def get_crypto_price(crypto: str) -> str:
    """获取加密货币价格（模拟真实 API）
    
    Args:
        crypto: 加密货币代码，如 BTC, ETH
    
    实际使用时可以调用真实 API：
    import requests
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd")
    """
    # 模拟数据
    mock_data = {
        "BTC": "比特币 (BTC): $43,256.78 ↑ +3.2%",
        "ETH": "以太坊 (ETH): $2,287.43 ↑ +2.1%",
        "SOL": "Solana (SOL): $98.32 ↑ +5.6%",
    }
    return mock_data.get(crypto.upper(), f"{crypto} 价格暂时无法获取")


def translate_text_api(text: str, target_lang: str = "en") -> str:
    """翻译文本（可接入真实翻译 API）
    
    Args:
        text: 要翻译的文本
        target_lang: 目标语言 (en/zh/ja/es/fr)
    
    实际使用时可以调用翻译 API：
    from googletrans import Translator
    translator = Translator()
    result = translator.translate(text, dest=target_lang)
    """
    # 模拟翻译
    translations = {
        "en": f"[English] {text}",
        "zh": f"[中文] {text}",
        "ja": f"[日本語] {text}",
    }
    return translations.get(target_lang, f"Translated to {target_lang}: {text}")


# ============================================================
# 第四部分：文件操作技能
# ============================================================

def save_to_file(filename: str, content: str) -> str:
    """保存内容到文件
    
    Args:
        filename: 文件名
        content: 要保存的内容
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"💾 内容已保存到文件: {filename}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"


def read_from_file(filename: str) -> str:
    """从文件读取内容
    
    Args:
        filename: 文件名
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"📄 文件内容:\n{content[:500]}..."  # 限制长度
    except FileNotFoundError:
        return f"❌ 文件不存在: {filename}"
    except Exception as e:
        return f"❌ 读取失败: {str(e)}"


# ============================================================
# 第五部分：组合使用 - 创建多技能代理
# ============================================================

def create_multi_skill_agent():
    """创建拥有多种技能的代理"""
    
    # 初始化带状态的技能
    notebook = NotebookSkill()
    task_manager = TaskManagerSkill()
    
    # 配置 DeepSeek 模型
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if api_key and api_key != "your_deepseek_api_key_here":
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"
        model = "openai:deepseek-chat"
    else:
        print("⚠️  未配置 DEEPSEEK_API_KEY，使用默认模型")
        model = "anthropic:claude-sonnet-4-5"
    
    print(f"🤖 创建多技能代理...")
    print(f"📋 模型: {model}")
    print(f"🛠️  技能列表:")
    print("  1. 股票查询")
    print("  2. 邮件发送")
    print("  3. 提醒创建")
    print("  4. 笔记管理")
    print("  5. 任务管理")
    print("  6. 加密货币查询")
    print("  7. 文件操作")
    print()
    
    # 创建代理，添加所有技能
    agent = create_agent(
        model=model,
        tools=[
            # 简单技能
            get_stock_price,
            send_email,
            create_reminder,
            get_crypto_price,
            # 带状态的技能
            notebook.add_note,
            notebook.get_note,
            notebook.list_notes,
            task_manager.add_task,
            task_manager.complete_task,
            task_manager.list_tasks,
            # 文件操作技能
            save_to_file,
            read_from_file,
        ],
        system_prompt="""你是一个功能强大的智能助手，拥有多种技能：

📈 **金融查询**：查询股票和加密货币价格
📧 **通讯功能**：发送邮件、创建提醒
📝 **知识管理**：笔记记录、任务管理
💾 **文件操作**：读写文件

请根据用户需求，灵活运用这些技能，提供专业、高效的服务。
在使用工具前，简要说明你的计划；完成后，给出清晰的结果总结。""",
    )
    
    return agent


# ============================================================
# 第六部分：测试与演示
# ============================================================

def demo_basic_skills():
    """演示基础技能"""
    print("=" * 70)
    print("【演示1】基础技能测试")
    print("=" * 70)
    
    agent = create_multi_skill_agent()
    
    test_queries = [
        "帮我查一下苹果(AAPL)的股票价格",
        "创建一个提醒，明天下午3点开会",
        "添加一个笔记，标题是'学习计划'，内容是'每天学习Python 2小时'",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[测试 {i}] 用户: {query}")
        print("-" * 70)
        try:
            response = agent.invoke({"messages": [{"role": "user", "content": query}]})
            # 提取最后一条消息
            if isinstance(response, dict) and "messages" in response:
                last_message = response["messages"][-1]
                if hasattr(last_message, 'content'):
                    print(f"助手: {last_message.content}")
                else:
                    print(f"助手: {last_message}")
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
    
    print("\n" + "=" * 70)


def demo_complex_workflow():
    """演示复杂工作流"""
    print("\n" + "=" * 70)
    print("【演示2】复杂工作流 - 任务管理")
    print("=" * 70)
    
    agent = create_multi_skill_agent()
    
    workflow_queries = [
        "添加3个任务：1.写代码（高优先级）2.开会（普通）3.看书（低优先级）",
        "查看所有待办任务",
        "完成第1个任务",
        "再查看一下任务列表",
    ]
    
    for i, query in enumerate(workflow_queries, 1):
        print(f"\n[步骤 {i}] 用户: {query}")
        print("-" * 70)
        try:
            response = agent.invoke({"messages": [{"role": "user", "content": query}]})
            if isinstance(response, dict) and "messages" in response:
                last_message = response["messages"][-1]
                if hasattr(last_message, 'content'):
                    print(f"助手: {last_message.content}")
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
    
    print("\n" + "=" * 70)


def main():
    """主函数"""
    print("=" * 70)
    print("🎓 LangChain 技能扩展教程")
    print("=" * 70)
    print()
    print("本教程展示了如何为 LangChain 代理添加新技能：")
    print()
    print("1️⃣  简单函数技能 - 直接定义函数")
    print("2️⃣  带状态技能 - 使用类封装")
    print("3️⃣  外部API集成 - 接入真实服务")
    print("4️⃣  文件操作技能 - 读写文件")
    print("5️⃣  组合使用 - 创建多技能代理")
    print()
    print("=" * 70)
    
    try:
        # 演示基础技能
        demo_basic_skills()
        
        # 演示复杂工作流
        demo_complex_workflow()
        
        print("\n" + "=" * 70)
        print("✅ 教程演示完成！")
        print()
        print("💡 添加新技能的步骤：")
        print("  1. 定义技能函数（带 docstring 说明参数）")
        print("  2. 将函数添加到 create_agent 的 tools 列表")
        print("  3. 更新 system_prompt 告诉代理有哪些技能")
        print("  4. 测试新技能是否工作正常")
        print()
        print("📖 查看源代码了解更多细节！")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ 运行错误: {str(e)}")
        print("\n请检查:")
        print("1. API Key 是否配置正确")
        print("2. 网络连接是否正常")


if __name__ == "__main__":
    main()
