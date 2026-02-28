# 🛠️ 技能扩展指南

本指南教你如何为 LangChain 代理添加新的技能（工具）。

## 📚 目录

1. [快速开始](#快速开始)
2. [技能类型](#技能类型)
3. [添加技能的步骤](#添加技能的步骤)
4. [最佳实践](#最佳实践)
5. [常见问题](#常见问题)

---

## 🚀 快速开始

### 运行示例

```bash
# 1. 查看完整教程
python skills_tutorial.py

# 2. 使用自定义技能模板
python my_custom_skills.py
```

---

## 🎯 技能类型

### 1. 简单函数技能

最简单的技能形式，直接定义函数：

```python
def get_weather(city: str) -> str:
    """查询天气信息
    
    Args:
        city: 城市名称
    
    Returns:
        天气信息
    """
    return f"{city} 的天气是晴朗的"
```

**特点：**
- ✅ 简单直接
- ✅ 无状态
- ✅ 适合单次调用

### 2. 带状态的技能（使用类）

需要记录状态的复杂技能：

```python
class NotebookSkill:
    """笔记本技能"""
    
    def __init__(self):
        self.notes = {}
    
    def add_note(self, title: str, content: str) -> str:
        """添加笔记"""
        self.notes[title] = content
        return f"笔记已保存: {title}"
    
    def get_note(self, title: str) -> str:
        """获取笔记"""
        return self.notes.get(title, "未找到笔记")

# 使用时先实例化
notebook = NotebookSkill()

# 然后将方法添加到 tools
tools = [notebook.add_note, notebook.get_note]
```

**特点：**
- ✅ 可以保持状态
- ✅ 多个相关功能组合
- ✅ 适合复杂场景

### 3. 外部 API 集成

连接真实的外部服务：

```python
def get_weather_real(city: str) -> str:
    """查询真实天气（接入天气API）"""
    import requests
    
    # 示例：接入和风天气API
    api_key = "your_api_key"
    url = f"https://api.qweather.com/v7/weather/now"
    params = {
        "location": city,
        "key": api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return f"{city} 天气: {data['now']['text']}, 温度: {data['now']['temp']}°C"
```

**常见 API 集成：**
- 🌤️ 天气 API
- 💱 汇率 API
- 📈 股票 API
- 🔍 搜索 API
- 🗺️ 地图 API

---

## 📝 添加技能的步骤

### 第一步：定义技能函数

```python
def my_new_skill(param1: str, param2: int = 10) -> str:
    """技能描述（这很重要！AI 会读取这个）
    
    Args:
        param1: 参数1的说明
        param2: 参数2的说明（可选参数）
    
    Returns:
        返回值说明
    """
    # 实现你的逻辑
    result = f"处理 {param1} 和 {param2}"
    return result
```

**重要提示：**
- ✅ 必须有详细的 docstring
- ✅ 使用类型注解（str, int, bool 等）
- ✅ 说明每个参数的用途
- ✅ 返回 str 类型（推荐）

### 第二步：添加到代理

```python
from langchain.agents import create_agent

agent = create_agent(
    model="openai:deepseek-chat",
    tools=[
        my_new_skill,  # 👈 添加你的技能
        other_skill1,
        other_skill2,
    ],
    system_prompt="你是一个助手，拥有 my_new_skill 等技能...",
)
```

### 第三步：更新系统提示词

```python
system_prompt = """你是一个智能助手，拥有以下技能：

1. my_new_skill - 做某某事情
2. other_skill1 - 做另一件事
3. other_skill2 - 还能做这个

请根据用户需求选择合适的工具。"""
```

### 第四步：测试

```python
# 测试你的新技能
response = agent.invoke({
    "messages": [{"role": "user", "content": "使用新技能处理一下 ABC"}]
})
print(response)
```

---

## 💡 最佳实践

### ✅ DO - 推荐做法

1. **清晰的函数名**
   ```python
   # 好
   def get_stock_price(symbol: str) -> str:
       pass
   
   # 不好
   def func1(x: str) -> str:
       pass
   ```

2. **详细的文档字符串**
   ```python
   def translate(text: str, target_lang: str) -> str:
       """翻译文本到目标语言
       
       这个函数可以将输入的文本翻译成指定的语言。
       
       Args:
           text: 要翻译的文本内容
           target_lang: 目标语言代码，如 'en', 'zh', 'ja'
       
       Returns:
           翻译后的文本
       
       Examples:
           >>> translate("Hello", "zh")
           "你好"
       """
   ```

3. **错误处理**
   ```python
   def safe_divide(a: float, b: float) -> str:
       """安全的除法运算"""
       try:
           result = a / b
           return f"{a} / {b} = {result}"
       except ZeroDivisionError:
           return "错误：不能除以零"
       except Exception as e:
           return f"错误：{str(e)}"
   ```

4. **返回有用的信息**
   ```python
   # 好 - 返回结构化信息
   def get_user_info(user_id: str) -> str:
       return f"""用户信息：
       ID: {user_id}
       姓名: 张三
       邮箱: zhang@example.com
       """
   
   # 不好 - 返回过于简单
   def get_user_info(user_id: str) -> str:
       return "张三"
   ```

### ❌ DON'T - 避免做法

1. **不要使用复杂的返回类型**
   ```python
   # 不推荐
   def bad_skill() -> Dict[str, List[Tuple]]:
       return {"data": [("a", 1), ("b", 2)]}
   
   # 推荐 - 返回字符串
   def good_skill() -> str:
       return "数据: a=1, b=2"
   ```

2. **不要遗漏文档**
   ```python
   # 不好 - 没有说明
   def mystery_function(x):
       return x * 2
   ```

3. **不要有副作用**
   ```python
   # 不好 - 会修改全局状态
   global_list = []
   def bad_skill(item: str) -> str:
       global_list.append(item)  # 副作用
       return "Done"
   
   # 好 - 使用类管理状态
   class GoodSkill:
       def __init__(self):
           self.items = []
       
       def add_item(self, item: str) -> str:
           self.items.append(item)
           return f"已添加: {item}"
   ```

---

## 🎨 技能示例集合

### 实用工具类

```python
# 1. 时间日期
def get_current_time(timezone: str = "Asia/Shanghai") -> str:
    """获取当前时间"""
    from datetime import datetime
    import pytz
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")

# 2. 文本处理
def reverse_text(text: str) -> str:
    """反转文本"""
    return text[::-1]

# 3. 编码转换
def url_encode(text: str) -> str:
    """URL 编码"""
    from urllib.parse import quote
    return quote(text)
```

### 数据处理类

```python
# 1. JSON 处理
def parse_json(json_str: str) -> str:
    """解析 JSON 字符串"""
    import json
    data = json.loads(json_str)
    return json.dumps(data, indent=2, ensure_ascii=False)

# 2. CSV 处理
def csv_to_table(csv_data: str) -> str:
    """将 CSV 转换为表格"""
    import csv
    from io import StringIO
    # 处理逻辑...
    pass
```

### 系统操作类

```python
# 1. 文件操作
def list_files(directory: str = ".") -> str:
    """列出目录中的文件"""
    import os
    files = os.listdir(directory)
    return "\n".join(files)

# 2. 环境信息
def get_system_info() -> str:
    """获取系统信息"""
    import platform
    return f"""系统信息：
    操作系统: {platform.system()}
    版本: {platform.version()}
    Python: {platform.python_version()}
    """
```

---

## ❓ 常见问题

### Q1: 为什么我的技能没有被调用？

**可能原因：**
1. 缺少或不清晰的 docstring
2. 参数类型注解缺失
3. system_prompt 没有提到这个技能
4. 函数名不够直观

**解决方案：**
```python
# 改进前
def func(x):
    return x * 2

# 改进后
def double_number(number: float) -> str:
    """将数字翻倍
    
    Args:
        number: 要翻倍的数字
    
    Returns:
        翻倍后的结果
    """
    result = number * 2
    return f"{number} 的两倍是 {result}"
```

### Q2: 如何传递复杂参数？

**使用 JSON 字符串：**
```python
def process_data(data_json: str) -> str:
    """处理复杂数据
    
    Args:
        data_json: JSON格式的数据，如 '{"name": "张三", "age": 25}'
    """
    import json
    data = json.loads(data_json)
    # 处理 data
    return f"已处理 {data['name']} 的数据"
```

### Q3: 如何调用外部 API？

**示例：**
```python
def search_github(query: str) -> str:
    """搜索 GitHub 仓库"""
    import requests
    
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc"}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        results = []
        for item in data["items"][:5]:
            results.append(f"- {item['name']}: {item['description']}")
        
        return "\n".join(results)
    except Exception as e:
        return f"搜索失败: {str(e)}"
```

### Q4: 如何管理多个相关技能？

**使用类组织：**
```python
class DatabaseSkill:
    """数据库操作技能集合"""
    
    def __init__(self):
        self.connection = None
    
    def connect(self, db_path: str) -> str:
        """连接数据库"""
        pass
    
    def query(self, sql: str) -> str:
        """执行查询"""
        pass
    
    def insert(self, table: str, data: str) -> str:
        """插入数据"""
        pass

# 使用
db_skill = DatabaseSkill()
tools = [db_skill.connect, db_skill.query, db_skill.insert]
```

---

## 🎓 进阶主题

### 异步技能

```python
import asyncio

async def fetch_data_async(url: str) -> str:
    """异步获取数据"""
    # 异步实现
    pass

# 注意：LangChain 支持异步工具
```

### 带验证的技能

```python
def validated_skill(param: str) -> str:
    """带参数验证的技能"""
    if not param:
        return "错误：参数不能为空"
    
    if len(param) > 100:
        return "错误：参数过长"
    
    # 正常处理
    return f"处理结果: {param}"
```

### 技能链

```python
def skill_a(input: str) -> str:
    """技能A"""
    return f"A({input})"

def skill_b(input: str) -> str:
    """技能B，可以使用技能A的结果"""
    result_a = skill_a(input)
    return f"B({result_a})"
```

---

## 📖 参考资源

- **LangChain 官方文档**: https://python.langchain.com/
- **工具定义指南**: https://python.langchain.com/docs/modules/agents/tools/
- **自定义工具教程**: https://python.langchain.com/docs/modules/agents/tools/custom_tools

---

## 💬 获取帮助

如果遇到问题：

1. 查看 `skills_tutorial.py` 中的示例
2. 运行 `python my_custom_skills.py` 测试模板
3. 检查函数的 docstring 和类型注解
4. 确保 system_prompt 描述了新技能

祝你构建出强大的 AI 助手！🚀
