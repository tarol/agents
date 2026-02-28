#!/usr/bin/env python
"""
示例1：基础代理使用
"""
import sys
sys.path.insert(0, '/Users/tarol/workspace/mine/line')

from src.agents import AgentFactory
from src.utils import print_header, print_separator, extract_response


def main():
    """基础代理示例"""
    print_header("示例1：基础代理")
    
    # 创建基础代理
    agent = AgentFactory.create_basic_agent()
    
    # 测试
    test_queries = [
        "深圳今天天气如何？",
        "计算 2024 * 365",
    ]
    
    for query in test_queries:
        print(f"\n用户: {query}")
        print_separator()
        response = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"助手: {extract_response(response)}")
    
    print("\n✅ 示例完成！")


if __name__ == "__main__":
    main()
