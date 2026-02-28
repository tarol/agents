#!/usr/bin/env python
"""
示例2：高级代理使用
"""
import sys
sys.path.insert(0, '/Users/tarol/workspace/mine/line')

from src.agents import AgentFactory
from src.utils import print_header, print_separator, extract_response


def main():
    """高级代理示例"""
    print_header("示例2：高级代理（全功能）")
    
    # 创建高级代理
    agent = AgentFactory.create_advanced_agent()
    
    # 测试
    test_queries = [
        "现在几点了？",
        "帮我创建一个提醒，明天下午3点开会",
        "查一下上海的天气",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[测试 {i}] 用户: {query}")
        print_separator()
        response = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"助手: {extract_response(response)}")
    
    print("\n✅ 示例完成！")


if __name__ == "__main__":
    main()
