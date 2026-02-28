"""
技能管理模块
"""
from .basic_skills import BASIC_SKILLS
from .advanced_skills import ADVANCED_SKILLS

__all__ = [
    'BASIC_SKILLS',
    'ADVANCED_SKILLS',
    'get_all_skills',
]


def get_all_skills():
    """获取所有技能"""
    return BASIC_SKILLS + ADVANCED_SKILLS
