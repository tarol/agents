"""
Agent 定义模块
存放所有预定义的 Agent 配置
"""
from . import basic_agent
from . import advanced_agent
from . import custom_agent


# 所有可用的 Agent 定义
AVAILABLE_AGENTS = [
    basic_agent,
    advanced_agent,
    custom_agent,
]


def get_all_agent_definitions():
    """获取所有 Agent 定义"""
    return AVAILABLE_AGENTS


def get_agent_by_id(agent_id: str):
    """根据 ID 获取 Agent 定义
    
    Args:
        agent_id: Agent ID
        
    Returns:
        Agent 定义模块，如果未找到则返回 None
    """
    for agent_module in AVAILABLE_AGENTS:
        info = agent_module.get_agent_info()
        if info["id"] == agent_id:
            return agent_module
    return None


__all__ = [
    'AVAILABLE_AGENTS',
    'get_all_agent_definitions',
    'get_agent_by_id',
    'basic_agent',
    'advanced_agent',
    'custom_agent',
]
