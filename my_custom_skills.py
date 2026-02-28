"""
自定义技能模板
在这里添加你自己的技能（工具）

使用步骤：
1. 在这个文件中定义新的技能函数
2. 在 create_my_agent() 中将技能添加到 tools 列表
3. 运行 python my_custom_skills.py 测试
"""
import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


# ============================================================
# 📝 在这里添加你的自定义技能
# ============================================================

def my_first_skill(query: str) -> str:
    """你的第一个自定义技能
    
    这是一个模板，你可以修改它来实现自己的功能
    
    Args:
        query: 用户的查询内容
    
    Returns:
        处理结果
    """
    # 在这里实现你的逻辑
    return f"收到查询: {query}\n这是你的第一个自定义技能的响应！"


def calculator_advanced(expression: str) -> str:
    """高级计算器 - 支持更多数学函数
    
    Args:
        expression: 数学表达式，支持 sin, cos, sqrt 等
    
    Returns:
        计算结果
    
    示例：
        calculator_advanced("2 ** 10")  # 2的10次方
        calculator_advanced("sqrt(16)")  # 平方根
    """
    import math
    try:
        # 安全的数学计算环境
        safe_dict = {
            "abs": abs,
            "round": round,
            "max": max,
            "min": min,
            "sum": sum,
            "pow": pow,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi,
            "e": math.e,
        }
        result = eval(expression, {"__builtins__": {}}, safe_dict)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


def word_counter(text: str) -> str:
    """统计文本信息
    
    Args:
        text: 要分析的文本
    
    Returns:
        文本统计信息
    """
    char_count = len(text)
    word_count = len(text.split())
    line_count = len(text.split('\n'))
    
    return f"""📊 文本统计：
    - 字符数: {char_count}
    - 单词数: {word_count}
    - 行数: {line_count}
    """


def url_shortener(url: str) -> str:
    """短链接生成（模拟）
    
    Args:
        url: 要缩短的URL
    
    Returns:
        短链接
    
    实际使用时可以接入真实的短链接API：
    - bit.ly API
    - TinyURL API
    - 自建短链服务
    """
    import hashlib
    # 模拟生成短链接
    hash_part = hashlib.md5(url.encode()).hexdigest()[:6]
    short_url = f"https://short.link/{hash_part}"
    return f"✂️ 短链接已生成:\n原链接: {url}\n短链接: {short_url}"


def qr_code_generator(content: str) -> str:
    """生成二维码信息（模拟）
    
    Args:
        content: 要生成二维码的内容
    
    Returns:
        二维码生成结果
    
    实际使用时可以使用 qrcode 库：
    import qrcode
    qr = qrcode.make(content)
    qr.save('qrcode.png')
    """
    return f"🔲 二维码已生成\n内容: {content}\n提示: 实际使用时可以调用 qrcode 库生成真实的二维码图片"


def random_generator(type: str = "number", count: int = 1) -> str:
    """随机内容生成器
    
    Args:
        type: 生成类型 (number/password/uuid)
        count: 生成数量
    
    Returns:
        随机生成的内容
    """
    import random
    import string
    import uuid
    
    if type == "number":
        results = [random.randint(1, 100) for _ in range(count)]
        return f"🎲 随机数字: {', '.join(map(str, results))}"
    
    elif type == "password":
        passwords = []
        for _ in range(count):
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choice(chars) for _ in range(12))
            passwords.append(password)
        return f"🔐 随机密码:\n" + "\n".join(passwords)
    
    elif type == "uuid":
        uuids = [str(uuid.uuid4()) for _ in range(count)]
        return f"🆔 UUID:\n" + "\n".join(uuids)
    
    else:
        return f"❌ 不支持的类型: {type}"


def json_formatter(json_string: str) -> str:
    """JSON 格式化工具
    
    Args:
        json_string: JSON 字符串
    
    Returns:
        格式化后的 JSON
    """
    import json
    try:
        data = json.loads(json_string)
        formatted = json.dumps(data, indent=2, ensure_ascii=False)
        return f"✨ 格式化后的 JSON:\n```json\n{formatted}\n```"
    except json.JSONDecodeError as e:
        return f"❌ JSON 解析错误: {str(e)}"


def base64_tool(text: str, mode: str = "encode") -> str:
    """Base64 编码/解码工具
    
    Args:
        text: 要处理的文本
        mode: 模式 (encode/decode)
    
    Returns:
        处理结果
    """
    import base64
    try:
        if mode == "encode":
            encoded = base64.b64encode(text.encode()).decode()
            return f"🔒 Base64 编码:\n{encoded}"
        elif mode == "decode":
            decoded = base64.b64decode(text.encode()).decode()
            return f"🔓 Base64 解码:\n{decoded}"
        else:
            return f"❌ 不支持的模式: {mode}"
    except Exception as e:
        return f"❌ 处理错误: {str(e)}"


# ============================================================
# 🤖 创建你的自定义代理
# ============================================================

def create_my_agent():
    """创建自定义代理
    
    在这里配置你的代理，添加所需的技能
    """
    
    # 配置模型
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if api_key and api_key != "your_deepseek_api_key_here":
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"
        model = "openai:deepseek-chat"
    else:
        model = "anthropic:claude-sonnet-4-5"
    
    print(f"🤖 使用模型: {model}")
    print(f"🛠️  加载自定义技能...\n")
    
    # 创建代理，在这里添加你的技能
    agent = create_agent(
        model=model,
        tools=[
            # 👇 在这里添加你的技能函数
            my_first_skill,
            calculator_advanced,
            word_counter,
            url_shortener,
            qr_code_generator,
            random_generator,
            json_formatter,
            base64_tool,
            # 继续添加更多技能...
        ],
        system_prompt="""你是一个功能丰富的智能助手，拥有以下技能：

🧮 **计算工具**：高级计算器，支持数学函数
📊 **文本分析**：统计字符、单词、行数
🔗 **链接工具**：生成短链接、二维码
🎲 **随机生成**：随机数、密码、UUID
💾 **数据工具**：JSON格式化、Base64编解码

请根据用户需求，选择合适的工具提供服务。回答要专业、准确、友好。""",
    )
    
    return agent


# ============================================================
# 🧪 测试你的技能
# ============================================================

def test_custom_skills():
    """测试自定义技能"""
    print("=" * 70)
    print("🧪 测试自定义技能")
    print("=" * 70)
    
    agent = create_my_agent()
    
    # 在这里添加测试查询
    test_queries = [
        "帮我计算 2 的 10 次方",
        "统计一下这段文字的信息：Hello World! This is a test.",
        "生成3个随机密码",
        "把这个JSON格式化：{\"name\":\"张三\",\"age\":25,\"city\":\"北京\"}",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[测试 {i}] 用户: {query}")
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
    print("✅ 测试完成！")
    print()
    print("💡 提示：")
    print("  1. 查看源代码了解如何添加新技能")
    print("  2. 修改 tools 列表来启用/禁用技能")
    print("  3. 更新 system_prompt 来描述新技能")
    print("=" * 70)


def main():
    """主函数"""
    test_custom_skills()


if __name__ == "__main__":
    main()
