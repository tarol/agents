# 🎨 如何添加新的 Agent

## 📋 步骤

### 1. 创建 Agent 定义文件

在 `src/agents/definitions/` 文件夹下创建新的 Python 文件，例如 `my_agent.py`：

```bash
cd src/agents/definitions/
cp _template.py my_agent.py
```

### 2. 编辑 Agent 定义

打开 `my_agent.py`，修改以下内容：

```python
"""
我的专属 Agent
描述你的 Agent 的功能和特点
"""
from ...skills import BASIC_SKILLS, ADVANCED_SKILLS

# Agent 元数据
AGENT_INFO = {
    "id": "my_agent",              # 唯一 ID
    "name": "我的专属 Agent",       # 显示名称
    "description": "专注于XXX的智能助手",  # 描述
    "icon": "🎯",                  # 图标
    "version": "1.0.0",
    "author": "Your Name",
}

# Agent 配置
AGENT_CONFIG = {
    "tools": BASIC_SKILLS + ADVANCED_SKILLS[:2],  # 自定义技能组合
    "system_prompt": """你是一个专注于XXX的智能助手。
    
    你的能力：
    - 能力1
    - 能力2
    - 能力3
    
    工作原则：
    - 原则1
    - 原则2
    """,
}

def get_agent_info():
    return AGENT_INFO

def get_agent_config():
    return AGENT_CONFIG
```

### 3. 注册 Agent

编辑 `src/agents/definitions/__init__.py`，添加你的 Agent：

```python
from . import basic_agent
from . import advanced_agent
from . import custom_agent
from . import my_agent  # 添加这行

# 在列表中添加
AVAILABLE_AGENTS = [
    basic_agent,
    advanced_agent,
    custom_agent,
    my_agent,  # 添加这行
]
```

### 4. 测试

运行程序，你的新 Agent 会自动出现在列表中：

```bash
python main.py
```

## 🎯 配置说明

### Agent 元数据 (AGENT_INFO)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | string | 唯一标识符 | "my_agent" |
| name | string | 显示名称 | "我的专属 Agent" |
| description | string | 简短描述 | "专注于数据分析的助手" |
| icon | string | 图标（emoji） | "🎯" |
| version | string | 版本号 | "1.0.0" |
| author | string | 作者 | "Your Name" |

### Agent 配置 (AGENT_CONFIG)

| 字段 | 类型 | 说明 |
|------|------|------|
| tools | list | 技能列表，从 `src/skills` 导入 |
| system_prompt | string | 系统提示词，定义 Agent 的行为 |

## 💡 技能组合示例

### 使用基础技能
```python
from ...skills import BASIC_SKILLS

AGENT_CONFIG = {
    "tools": BASIC_SKILLS,
    ...
}
```

### 使用全部技能
```python
from ...skills import get_all_skills

AGENT_CONFIG = {
    "tools": get_all_skills(),
    ...
}
```

### 自定义技能组合
```python
from ...skills import BASIC_SKILLS, ADVANCED_SKILLS

AGENT_CONFIG = {
    "tools": BASIC_SKILLS[:2] + ADVANCED_SKILLS[1:3],  # 选择特定技能
    ...
}
```

### 使用单个技能
```python
from ...skills.basic_skills import get_weather, calculate

AGENT_CONFIG = {
    "tools": [get_weather, calculate],  # 只使用天气和计算
    ...
}
```

## 📝 System Prompt 编写技巧

好的 system prompt 应该包含：

1. **角色定义**：Agent 是谁
2. **能力说明**：Agent 能做什么
3. **行为准则**：Agent 应该如何回应
4. **限制说明**：Agent 不能做什么（可选）

### 示例

```python
system_prompt = """你是一个专业的数据分析助手。

🎯 你的专长：
- 数据清洗和格式化
- 统计分析和可视化
- 趋势预测和洞察发现

📋 工作原则：
1. 始终确保数据的准确性
2. 提供清晰的分析思路
3. 用可视化辅助说明
4. 给出可操作的建议

⚠️ 注意事项：
- 对不确定的数据要说明
- 避免过度解读数据
- 保护数据隐私和安全
"""
```

## 🚀 高级用法

### 动态配置

可以让 Agent 配置根据环境变量或条件变化：

```python
import os

def get_agent_config():
    # 根据环境调整配置
    if os.getenv("EXPERT_MODE") == "true":
        tools = get_all_skills()
    else:
        tools = BASIC_SKILLS
    
    return {
        "tools": tools,
        "system_prompt": "...",
    }
```

### 多版本 Agent

可以创建同一 Agent 的不同版本：

```
definitions/
  ├── analyst_basic.py    # 基础版分析师
  ├── analyst_pro.py      # 专业版分析师
  └── analyst_expert.py   # 专家版分析师
```

## 📚 参考

- 查看 `basic_agent.py` - 简单的 Agent 示例
- 查看 `advanced_agent.py` - 功能完整的 Agent 示例
- 查看 `custom_agent.py` - 自定义配置的 Agent 示例

## ❓ 常见问题

**Q: 如何删除 Agent？**  
A: 从 `__init__.py` 的 `AVAILABLE_AGENTS` 列表中移除，或删除定义文件

**Q: Agent 的顺序如何修改？**  
A: 调整 `__init__.py` 中 `AVAILABLE_AGENTS` 列表的顺序

**Q: 可以动态加载 Agent 吗？**  
A: 当前是静态导入，如需动态加载可以修改 `loader.py` 实现文件扫描

**Q: 如何给 Agent 添加状态？**  
A: 可以在定义文件中添加额外的配置字段，然后在 `loader.py` 中处理
