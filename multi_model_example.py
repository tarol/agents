"""
多模型支持示例
展示如何在 LangChain 中使用不同的大语言模型
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

# 加载环境变量
load_dotenv()


def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
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


def get_model_config():
    """根据环境变量获取模型配置"""
    provider = os.getenv("MODEL_PROVIDER", "anthropic").lower()
    
    model_configs = {
        "anthropic": {
            "model": "anthropic:claude-sonnet-4-5",
            "name": "Anthropic Claude Sonnet 4.5",
            "env_key": "ANTHROPIC_API_KEY",
        },
        "openai": {
            "model": "openai:gpt-4o",
            "name": "OpenAI GPT-4o",
            "env_key": "OPENAI_API_KEY",
        },
        "google": {
            "model": "google:gemini-2.0-flash-exp",
            "name": "Google Gemini 2.0 Flash",
            "env_key": "GOOGLE_API_KEY",
        },
        "deepseek": {
            "model": "openai:deepseek-chat",
            "name": "DeepSeek V3 (推荐)",
            "env_key": "DEEPSEEK_API_KEY",
            "base_url": "https://api.deepseek.com",
        },
        "dashscope": {
            "model": "dashscope:qwen-max",
            "name": "阿里云通义千问 Max",
            "env_key": "DASHSCOPE_API_KEY",
        },
        "zhipuai": {
            "model": "zhipuai:glm-4",
            "name": "智谱 ChatGLM-4",
            "env_key": "ZHIPUAI_API_KEY",
        },
    }
    
    return model_configs.get(provider, model_configs["anthropic"])


def create_agent_with_model(model_name: str = None, base_url: str = None):
    """创建使用指定模型的代理"""
    
    if model_name:
        config = {"model": model_name, "name": model_name, "base_url": base_url}
    else:
        config = get_model_config()
    
    print(f"🤖 使用模型: {config['name']}")
    print(f"📋 模型标识: {config['model']}")
    
    # 处理 DeepSeek 的特殊配置
    model_str = config["model"]
    if config.get("base_url"):
        print(f"🌐 API 地址: {config['base_url']}")
        # DeepSeek 需要设置环境变量
        if "deepseek" in config["name"].lower():
            os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY", "")
            os.environ["OPENAI_API_BASE"] = config["base_url"]
    
    # 创建代理
    agent = create_agent(
        model=model_str,
        tools=[get_weather, calculate],
        system_prompt="""你是一个乐于助人的智能助手。你可以：
        1. 查询天气信息
        2. 进行数学计算
        
        请根据用户的问题，选择合适的工具来回答。回答要简洁、准确、友好。""",
    )
    
    return agent


def compare_models():
    """对比不同模型的响应"""
    print("=" * 70)
    print("LangChain 多模型对比示例")
    print("=" * 70)
    
    # 可用的模型列表
    available_models = []
    
    if os.getenv("DEEPSEEK_API_KEY"):
        available_models.append(("openai:deepseek-chat", "DeepSeek V3", "https://api.deepseek.com"))
    if os.getenv("ANTHROPIC_API_KEY"):
        available_models.append(("anthropic:claude-sonnet-4-5", "Anthropic Claude", None))
    if os.getenv("OPENAI_API_KEY"):
        available_models.append(("openai:gpt-4o", "OpenAI GPT-4o", None))
    if os.getenv("GOOGLE_API_KEY"):
        available_models.append(("google:gemini-2.0-flash-exp", "Google Gemini", None))
    
    if not available_models:
        print("\n❌ 错误: 请至少配置一个模型的 API Key")
        print("\n请编辑 .env 文件，填入以下任一 API Key:")
        print("  - DEEPSEEK_API_KEY (推荐)")
        print("  - ANTHROPIC_API_KEY")
        print("  - OPENAI_API_KEY")
        print("  - GOOGLE_API_KEY")
        return
    
    print(f"\n✅ 检测到 {len(available_models)} 个可用模型\n")
    
    # 测试问题
    query = "上海的天气怎么样？"
    
    # 对比每个模型的响应
    for model_info in available_models:
        model_id = model_info[0]
        model_name = model_info[1]
        base_url = model_info[2] if len(model_info) > 2 else None
        
        print("\n" + "=" * 70)
        print(f"📍 模型: {model_name}")
        print("-" * 70)
        print(f"用户: {query}")
        print("-" * 70)
        
        try:
            # 特殊处理 DeepSeek
            if "deepseek" in model_name.lower() and base_url:
                os.environ["OPENAI_API_KEY"] = os.getenv("DEEPSEEK_API_KEY", "")
                os.environ["OPENAI_API_BASE"] = base_url
            
            agent = create_agent_with_model(model_id, base_url)
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print(f"助手: {response}")
        except Exception as e:
            print(f"❌ 错误: {str(e)}")


def single_model_demo():
    """使用配置的单个模型进行演示"""
    print("=" * 70)
    print("LangChain 智能代理 - 多模型支持")
    print("=" * 70)
    
    try:
        # 创建代理
        agent = create_agent_with_model()
        
        print("\n" + "=" * 70)
        
        # 测试问题
        test_queries = [
            "北京的天气怎么样？",
            "帮我计算 256 * 384",
        ]
        
        for query in test_queries:
            print(f"\n用户: {query}")
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
        print("=" * 70)
        
    except Exception as e:
        print(f"\n❌ 初始化错误: {str(e)}")
        print("\n请检查:")
        print("1. .env 文件中对应的 API Key 是否正确配置")
        print("2. MODEL_PROVIDER 设置是否正确")


def main():
    """主函数"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--compare":
        # 对比模式
        compare_models()
    else:
        # 单模型演示模式
        single_model_demo()
        print("\n💡 提示: 使用 'python multi_model_example.py --compare' 可对比多个模型")


if __name__ == "__main__":
    main()
