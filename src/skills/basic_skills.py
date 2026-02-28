"""
基础技能模块
包含常用的基础工具
"""


def get_weather(city: str) -> str:
    """获取指定城市的天气信息
    
    Args:
        city: 城市名称
    
    Returns:
        天气信息
    """
    weather_data = {
        "北京": "多云，温度 15°C，空气质量良好",
        "上海": "晴朗，温度 20°C，适合外出",
        "深圳": "阴天，温度 25°C，湿度较高",
        "杭州": "小雨，温度 18°C，记得带伞",
        "成都": "多云转晴，温度 22°C，天气宜人",
    }
    return weather_data.get(city, f"{city} 天气晴朗，温度适宜！")


def calculate(expression: str) -> str:
    """计算数学表达式
    
    Args:
        expression: 数学表达式
    
    Returns:
        计算结果
    """
    try:
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


def search_info(query: str) -> str:
    """搜索信息（模拟）
    
    Args:
        query: 搜索关键词
    
    Returns:
        搜索结果
    """
    return f"关于 '{query}' 的搜索结果：这是一个模拟的搜索结果。在实际应用中，这里会返回真实的搜索信息。"


# 导出所有基础技能
BASIC_SKILLS = [
    get_weather,
    calculate,
    search_info,
]
