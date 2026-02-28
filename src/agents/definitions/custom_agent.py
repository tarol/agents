"""
自定义 Agent 定义
可以根据需求自定义技能组合
"""
from ...skills import BASIC_SKILLS


# Agent 元数据
AGENT_INFO = {
    "id": "custom",
    "name": "自定义 Agent",
    "description": "专注于天气和计算的精简助手",
    "icon": "⚙️",
    "version": "1.0.0",
    "author": "User",
}


# Agent 配置
AGENT_CONFIG = {
    "tools": BASIC_SKILLS[:2],  # 只使用前两个技能：天气和计算
    "system_prompt": """你是一个专注于天气查询和数学计算的助手。
    
    你的专长领域：
    🌤️  天气查询 - 提供准确的天气信息
    🔢  数学计算 - 快速计算各种数学表达式
    
    请专注于这两个领域，提供专业的服务。""",
}


def get_agent_info():
    """获取 Agent 信息"""
    return AGENT_INFO


def get_agent_config():
    """获取 Agent 配置"""
    return AGENT_CONFIG
