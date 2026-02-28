"""
Agent 定义模板
复制此文件创建新的 Agent 定义
"""
from ...skills import BASIC_SKILLS  # 根据需要导入技能


# Agent 元数据
AGENT_INFO = {
    "id": "template",  # 唯一标识符，使用小写字母和下划线
    "name": "模板 Agent",  # 显示名称
    "description": "这是一个 Agent 模板",  # 简短描述
    "icon": "🤖",  # 显示图标（emoji）
    "version": "1.0.0",  # 版本号
    "author": "Your Name",  # 作者
}


# Agent 配置
AGENT_CONFIG = {
    "tools": BASIC_SKILLS,  # Agent 可用的工具列表
    "system_prompt": """你的系统提示词。
    
    在这里描述 Agent 的角色、能力和行为准则。
    可以使用多行文本。""",
}


def get_agent_info():
    """获取 Agent 信息"""
    return AGENT_INFO


def get_agent_config():
    """获取 Agent 配置"""
    return AGENT_CONFIG
