"""
LangChain 流式输出示例
展示如何使用流式处理来实时获取代理的响应
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

# 加载环境变量
load_dotenv()


def get_long_story(topic: str) -> str:
    """生成一个关于指定主题的故事"""
    return f"""这是一个关于{topic}的故事：
    
    很久很久以前，在一个遥远的地方，发生了一件有趣的事情。
    这个故事告诉我们，{topic}是多么的重要和有意义。
    通过不断的学习和实践，我们可以更好地理解{topic}的本质。
    """


def streaming_demo():
    """演示流式输出"""
    print("=" * 60)
    print("LangChain 流式输出演示")
    print("=" * 60)
    
    # 创建代理
    agent = create_agent(
        model="anthropic:claude-sonnet-4-5",
        tools=[get_long_story],
        system_prompt="你是一个会讲故事的助手，擅长用生动的语言描述各种主题。",
    )
    
    query = "给我讲一个关于人工智能的故事"
    print(f"\n用户: {query}")
    print("-" * 60)
    print("助手: ", end="", flush=True)
    
    try:
        # 使用流式输出
        for chunk in agent.stream(
            {"messages": [{"role": "user", "content": query}]}
        ):
            # 打印每个片段
            if isinstance(chunk, dict) and "content" in chunk:
                print(chunk["content"], end="", flush=True)
            elif isinstance(chunk, str):
                print(chunk, end="", flush=True)
        
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"\n错误: {str(e)}")


if __name__ == "__main__":
    streaming_demo()
