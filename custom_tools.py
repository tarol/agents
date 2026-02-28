"""
自定义工具示例
展示如何创建更复杂的自定义工具
"""
import os
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_current_time(timezone: str = "Asia/Shanghai") -> str:
    """获取当前时间"""
    current = datetime.now()
    return f"当前时间（{timezone}）: {current.strftime('%Y-%m-%d %H:%M:%S')}"


def format_data(data: str, format_type: str = "json") -> str:
    """格式化数据
    
    Args:
        data: 要格式化的数据
        format_type: 格式类型 (json, markdown, list)
    """
    if format_type == "json":
        return f'{{"data": "{data}", "formatted": true}}'
    elif format_type == "markdown":
        return f"### 数据\n\n- {data}"
    elif format_type == "list":
        return f"1. {data}"
    else:
        return data


def translate_text(text: str, target_lang: str = "en") -> str:
    """翻译文本（模拟）
    
    Args:
        text: 要翻译的文本
        target_lang: 目标语言 (en, zh, ja, es)
    """
    # 这是模拟翻译，实际应用中可以集成真实的翻译 API
    translations = {
        "en": f"[EN] Translated: {text}",
        "zh": f"[中文] 翻译：{text}",
        "ja": f"[日本語] 翻訳：{text}",
        "es": f"[ES] Traducido: {text}",
    }
    return translations.get(target_lang, f"Unsupported language: {target_lang}")


def create_todo_list(tasks: str) -> str:
    """创建待办事项列表
    
    Args:
        tasks: 任务描述，用逗号分隔
    """
    task_list = tasks.split(",")
    result = "📋 待办事项列表：\n\n"
    for i, task in enumerate(task_list, 1):
        result += f"{i}. [ ] {task.strip()}\n"
    return result


def advanced_tools_demo():
    """演示高级自定义工具"""
    print("=" * 60)
    print("LangChain 高级自定义工具演示")
    print("=" * 60)
    
    # 创建配备多个高级工具的代理
    agent = create_agent(
        model="anthropic:claude-sonnet-4-5",
        tools=[
            get_current_time,
            format_data,
            translate_text,
            create_todo_list,
        ],
        system_prompt="""你是一个多功能智能助手，可以：
        1. 获取当前时间
        2. 格式化数据
        3. 翻译文本（支持多种语言）
        4. 创建待办事项列表
        
        请根据用户需求，灵活组合使用这些工具。""",
    )
    
    # 测试查询
    test_queries = [
        "现在几点了？",
        "帮我把'学习Python, 练习LangChain, 构建AI应用'转换成待办事项列表",
        "将'Hello World'翻译成中文",
    ]
    
    for query in test_queries:
        print(f"\n用户: {query}")
        print("-" * 60)
        
        try:
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print(f"助手: {response}")
        except Exception as e:
            print(f"错误: {str(e)}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    advanced_tools_demo()
