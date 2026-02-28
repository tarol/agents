"""
DeepSeek 模型专用示例
展示如何使用 DeepSeek V3 模型 - 性价比超高的国产大模型
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# 加载环境变量
load_dotenv()


def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    weather_data = {
        "北京": "多云，温度 15°C，空气质量良好",
        "上海": "晴朗，温度 20°C，适合外出",
        "深圳": "阴天，温度 25°C，湿度较高",
        "杭州": "小雨，温度 18°C，记得带伞",
        "成都": "多云转晴，温度 22°C，天气宜人",
    }
    return weather_data.get(city, f"{city} 天气晴朗，温度适宜！")


def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


def get_code_suggestion(language: str, task: str) -> str:
    """获取编程建议（模拟）"""
    suggestions = {
        "python": f"对于 {task}，推荐使用 Python 的内置函数或标准库，代码简洁高效。",
        "javascript": f"在 JavaScript 中实现 {task}，建议使用 ES6+ 语法，代码更现代。",
        "java": f"Java 实现 {task} 时，注意使用合适的数据结构和设计模式。",
    }
    return suggestions.get(language.lower(), f"关于 {language} 的 {task}，建议参考官方文档。")


def create_deepseek_agent():
    """创建使用 DeepSeek 模型的代理"""
    
    # 检查 API Key
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key or api_key == "your_deepseek_api_key_here":
        raise ValueError(
            "请先配置 DEEPSEEK_API_KEY！\n"
            "1. 访问 https://platform.deepseek.com/ 注册账号\n"
            "2. 获取 API Key\n"
            "3. 在 .env 文件中设置: DEEPSEEK_API_KEY=your_key_here"
        )
    
    print("🤖 使用模型: DeepSeek V3")
    print("💰 特点: 性价比极高，性能优异")
    print("🌐 API 地址: https://api.deepseek.com")
    print()
    
    # 配置 DeepSeek
    # DeepSeek API 兼容 OpenAI 格式，使用 ChatOpenAI 类
    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key=api_key,
        openai_api_base="https://api.deepseek.com",
        temperature=0.7,
    )
    
    # 创建代理
    agent = create_agent(
        model=llm,
        tools=[get_weather, calculate, get_code_suggestion],
        system_prompt="""你是一个专业的智能助手，由 DeepSeek 提供支持。你可以：
        1. 查询天气信息
        2. 进行数学计算
        3. 提供编程建议
        
        请根据用户需求，灵活使用工具，给出专业、准确、友好的回答。""",
    )
    
    return agent


def main():
    """主函数"""
    print("=" * 70)
    print("DeepSeek V3 智能代理示例")
    print("=" * 70)
    
    try:
        # 创建代理
        agent = create_deepseek_agent()
        
        print("=" * 70)
        print("\n✅ DeepSeek 代理创建成功！开始测试...\n")
        
        # 测试问题
        test_queries = [
            "深圳今天天气怎么样？",
            "帮我计算 1234 * 5678",
            "我想用 Python 处理 JSON 数据，有什么建议？",
        ]
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n[测试 {i}/{len(test_queries)}]")
            print(f"用户: {query}")
            print("-" * 70)
            
            try:
                response = agent.invoke(
                    {"messages": [{"role": "user", "content": query}]}
                )
                print(f"助手: {response}")
            except Exception as e:
                print(f"❌ 错误: {str(e)}")
        
        print("\n" + "=" * 70)
        print("演示结束！")
        print("\n💡 DeepSeek 优势:")
        print("  • 价格低廉：仅为 GPT-4 的 1/10")
        print("  • 性能强大：接近 GPT-4 水平")
        print("  • 响应迅速：推理速度快")
        print("  • 中文优化：对中文理解出色")
        print("=" * 70)
        
    except ValueError as e:
        print(f"\n❌ 配置错误: {e}")
    except Exception as e:
        print(f"\n❌ 运行错误: {str(e)}")
        print("\n请检查:")
        print("1. DEEPSEEK_API_KEY 是否正确")
        print("2. 网络连接是否正常")
        print("3. API 余额是否充足")


if __name__ == "__main__":
    main()
