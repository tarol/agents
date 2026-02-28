"""
工具函数模块
"""


def print_header(title: str):
    """打印标题"""
    print("=" * 70)
    print(title)
    print("=" * 70)


def print_separator():
    """打印分隔线"""
    print("-" * 70)


def extract_response(response) -> str:
    """从代理响应中提取文本
    
    Args:
        response: 代理响应
    
    Returns:
        响应文本
    """
    if isinstance(response, dict) and "messages" in response:
        last_message = response["messages"][-1]
        if hasattr(last_message, 'content'):
            return last_message.content
        else:
            return str(last_message)
    return str(response)
