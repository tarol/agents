"""
高级技能模块
包含更复杂的工具
"""
import os
from datetime import datetime


def get_current_time(timezone: str = "Asia/Shanghai") -> str:
    """获取当前时间
    
    Args:
        timezone: 时区
    
    Returns:
        当前时间
    """
    current = datetime.now()
    return f"当前时间（{timezone}）: {current.strftime('%Y-%m-%d %H:%M:%S')}"


def create_reminder(task: str, time: str) -> str:
    """创建提醒事项
    
    Args:
        task: 提醒内容
        time: 提醒时间
    
    Returns:
        创建结果
    """
    return f"⏰ 提醒已创建\n任务: {task}\n时间: {time}\n将在指定时间通知您！"


def format_data(data: str, format_type: str = "json") -> str:
    """格式化数据
    
    Args:
        data: 要格式化的数据
        format_type: 格式类型 (json/markdown/list)
    
    Returns:
        格式化后的数据
    """
    if format_type == "json":
        return f'{{"data": "{data}", "formatted": true}}'
    elif format_type == "markdown":
        return f"### 数据\n\n- {data}"
    elif format_type == "list":
        return f"1. {data}"
    else:
        return data


def save_to_file(filename: str, content: str) -> str:
    """保存内容到文件
    
    Args:
        filename: 文件名
        content: 内容
    
    Returns:
        保存结果
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"💾 内容已保存到文件: {filename}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"


# 导出高级技能
ADVANCED_SKILLS = [
    get_current_time,
    create_reminder,
    format_data,
    save_to_file,
]
