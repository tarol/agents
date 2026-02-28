"""
高级 Agent 定义
提供全部技能，包括基础功能、时间管理、数据处理等
"""
from ...skills import get_all_skills


# Agent 元数据
AGENT_INFO = {
    "id": "advanced",
    "name": "高级 Agent",
    "description": "拥有全部技能：基础功能 + 时间管理 + 数据处理",
    "icon": "💎",
    "version": "1.0.0",
    "author": "System",
}


# Agent 配置
AGENT_CONFIG = {
    "tools": get_all_skills(),
    "system_prompt": """你是一个功能强大的智能助手，拥有多种技能：
    
    📊 **基础功能**：天气查询、数学计算、信息搜索
    ⏰ **时间管理**：获取时间、创建提醒
    💾 **数据处理**：格式化数据、文件操作
    
    请根据用户需求，灵活运用这些技能，提供专业、高效的服务。""",
}


def get_agent_info():
    """获取 Agent 信息"""
    return AGENT_INFO


def get_agent_config():
    """获取 Agent 配置"""
    return AGENT_CONFIG
