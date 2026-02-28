"""
LangChain 智能代理示例
这个示例展示了如何创建一个配备多个工具的智能代理
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

# 加载环境变量
load_dotenv()


def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    # 这里是模拟数据，实际应用中可以调用真实的天气 API
    weather_data = {
        "北京": "多云，温度 15°C",
        "上海": "晴朗，温度 20°C",
        "深圳": "阴天，温度 25°C",
        "旧金山": "晴朗，温度 18°C",
    }
    return weather_data.get(city, f"{city} 天气总是晴朗！温度适宜。")


def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


def search_info(query: str) -> str:
    """搜索信息（模拟）"""
    # 这里是模拟搜索，实际应用中可以集成真实的搜索 API
    return f"关于 '{query}' 的搜索结果：这是一个模拟的搜索结果。在实际应用中，这里会返回真实的搜索信息。"


def create_my_agent():
    """创建并配置智能代理"""
    
    # 从环境变量读取模型配置（默认使用 Anthropic）
    model_provider = os.getenv("MODEL_PROVIDER", "anthropic")
    
    # 模型映射
    model_map = {
        "anthropic": "anthropic:claude-sonnet-4-5",
        "openai": "openai:gpt-4o",
        "google": "google:gemini-2.0-flash-exp",
        "deepseek": "openai:deepseek-chat",
    }
    
    # DeepSeek 特殊配置
    if model_provider == "deepseek":
        os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY", "")
        os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"
    
    model_name = model_map.get(model_provider, "anthropic:claude-sonnet-4-5")
    print(f"🤖 使用模型: {model_name}\n")
    
    # 创建代理，配备多个工具
    agent = create_agent(
        model=model_name,
        tools=[get_weather, calculate, search_info],
        system_prompt="""你是一个乐于助人的智能助手。你可以：
        1. 查询天气信息
        2. 进行数学计算
        3. 搜索信息
        
        请根据用户的问题，选择合适的工具来回答。回答要简洁、准确、友好。""",
    )
    
    return agent


def main():
    """主函数"""
    print("=" * 60)
    print("欢迎使用 LangChain 智能代理！")
    print("=" * 60)
    
    # 创建代理
    agent = create_my_agent()
    
    # 示例对话
    test_queries = [
        "北京的天气怎么样？",
        "帮我计算 123 * 456",
        "搜索一下 LangChain 的最新功能",
    ]
    
    for query in test_queries:
        print(f"\n用户: {query}")
        print("-" * 60)
        
        try:
            # 调用代理
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print(f"助手: {response}")
        except Exception as e:
            print(f"错误: {str(e)}")
    
    print("\n" + "=" * 60)
    print("演示结束！")
    print("=" * 60)


if __name__ == "__main__":
    main()
