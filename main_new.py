#!/usr/bin/env python
"""
主程序 - 基础代理示例
"""
from src.agents import AgentFactory
from src.utils import print_header, print_separator, extract_response


def main():
    """主函数"""
    print_header("欢迎使用 LangChain 智能代理！")
    
    # 创建基础代理
    agent = AgentFactory.create_basic_agent()
    
    print_header("开始演示")
    
    # 测试问题
    test_queries = [
        "北京的天气怎么样？",
        "帮我计算 123 * 456",
        "搜索一下 LangChain 的最新功能",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[测试 {i}/{len(test_queries)}]")
        print(f"用户: {query}")
        print_separator()
        
        try:
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print(f"助手: {extract_response(response)}")
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
    
    print("\n" + "=" * 70)
    print("演示结束！")
    print("=" * 70)


if __name__ == "__main__":
    main()
