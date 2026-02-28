"""
基础 Agent 定义
提供天气查询、计算器、搜索等基础功能
"""
from ...skills import BASIC_SKILLS


# Agent 元数据
AGENT_INFO = {
    "id": "basic",
    "name": "基础 Agent",
    "description": "拥有基础技能：天气查询、计算器、搜索",
    "icon": "🔷",
    "version": "1.0.0",
    "author": "System",
}


# Agent 配置
AGENT_CONFIG = {
    "tools": BASIC_SKILLS,
    "system_prompt": """你是一个智能助手，拥有以下基础技能：
    1. 查询天气信息
    2. 进行数学计算
    3. 搜索信息
    
    请根据用户的问题，选择合适的工具来回答。回答要简洁、准确、友好。""",
}


def get_agent_info():
    """获取 Agent 信息"""
    return AGENT_INFO


def get_agent_config():
    """获取 Agent 配置"""
    return AGENT_CONFIG
