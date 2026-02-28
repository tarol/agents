#!/usr/bin/env python
"""
示例3：自定义代理
"""
import sys
sys.path.insert(0, '/Users/tarol/workspace/mine/line')

from src.agents import AgentFactory
from src.skills.basic_skills import get_weather, calculate
from src.utils import print_header, print_separator, extract_response


def custom_skill(query: str) -> str:
    """自定义技能示例"""
    return f"这是自定义技能的响应: {query}"


def main():
    """自定义代理示例"""
    print_header("示例3：自定义代理")
    
    # 创建自定义代理
    agent = AgentFactory.create_custom_agent(
        tools=[get_weather, calculate, custom_skill],
        system_prompt="你是一个自定义助手，可以查天气、做计算、使用自定义技能。"
    )
    
    # 测试
    query = "北京天气如何？"
    print(f"\n用户: {query}")
    print_separator()
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(f"助手: {extract_response(response)}")
    
    print("\n✅ 示例完成！")


if __name__ == "__main__":
    main()
