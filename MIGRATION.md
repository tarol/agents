# 项目结构重组说明

## ✅ 已完成的改进

项目已从扁平结构重组为专业的模块化结构！

### 📁 新的项目结构

```
line/
├── src/                         # 核心源代码
│   ├── config.py               # 配置管理（统一管理所有配置）
│   ├── agents/                 # 代理模块
│   │   └── agent_factory.py   # 代理工厂（统一创建代理）
│   ├── skills/                 # 技能模块
│   │   ├── basic_skills.py    # 基础技能（天气、计算、搜索）
│   │   └── advanced_skills.py # 高级技能（时间、提醒、文件）
│   └── utils/                  # 工具模块
│       └── helpers.py          # 辅助函数
│
├── examples/                    # 示例代码
│   ├── 01_basic_agent.py       # 基础代理示例
│   ├── 02_advanced_agent.py    # 高级代理示例
│   └── 03_custom_agent.py      # 自定义代理示例
│
├── docs/                        # 文档
│   └── SKILLS_GUIDE.md         # 技能扩展指南
│
├── config/                      # 配置文件
│   └── .env                    # 环境变量
│
├── main_new.py                 # 新版主程序（推荐使用）
├── README_NEW.md               # 新版README（推荐阅读）
│
└── 旧文件（保留，可选择删除）
    ├── main.py
    ├── deepseek_example.py
    ├── custom_tools.py
    ├── multi_model_example.py
    ├── skills_tutorial.py
    ├── my_custom_skills.py
    └── streaming_example.py
```

## 🎯 核心改进

### 1. 模块化设计
- **分离关注点**：配置、代理、技能、工具各自独立
- **易于维护**：每个模块职责清晰
- **便于测试**：可以单独测试每个模块

### 2. 统一管理
- **配置集中**：所有配置在 `src/config.py`
- **代理工厂**：通过工厂模式创建代理
- **技能组织**：按功能分类管理技能

### 3. 清晰的入口
- **新主程序**：`main_new.py`
- **示例代码**：`examples/` 目录下有多个示例
- **文档完善**：`README_NEW.md` 和 `SKILLS_GUIDE.md`

## 🚀 使用新结构

### 方式1：运行新主程序
```bash
python main_new.py
```

### 方式2：运行示例
```bash
# 基础代理
python examples/01_basic_agent.py

# 高级代理
python examples/02_advanced_agent.py

# 自定义代理
python examples/03_custom_agent.py
```

### 方式3：在代码中使用
```python
from src.agents import AgentFactory

# 创建代理
agent = AgentFactory.create_basic_agent()

# 使用代理
response = agent.invoke({
    "messages": [{"role": "user", "content": "你好"}]
})
```

## 📝 添加新技能（现在更简单！）

### 步骤1：在技能模块中添加
编辑 `src/skills/basic_skills.py`：

```python
def my_skill(param: str) -> str:
    """我的技能"""
    return f"处理: {param}"

# 添加到导出列表
BASIC_SKILLS = [
    get_weather,
    calculate,
    search_info,
    my_skill,  # 👈 添加这里
]
```

### 步骤2：直接使用
```python
from src.agents import AgentFactory

# 自动包含你的新技能
agent = AgentFactory.create_basic_agent()
```

## 🔄 迁移指南

### 从旧代码迁移

#### 旧方式：
```python
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()
agent = create_agent(...)
```

#### 新方式：
```python
from src.agents import AgentFactory

agent = AgentFactory.create_basic_agent()
```

更简单、更清晰！

## 🗑️ 旧文件处理

以下旧文件已被新结构替代，可以选择删除：

- `main.py` → 使用 `main_new.py`
- `deepseek_example.py` → 使用 `examples/01_basic_agent.py`
- `custom_tools.py` → 功能已整合到 `src/skills/`
- `multi_model_example.py` → 功能已整合到 `src/config.py`
- `skills_tutorial.py` → 使用 `docs/SKILLS_GUIDE.md` + 示例
- `my_custom_skills.py` → 使用 `examples/03_custom_agent.py`
- `streaming_example.py` → 后续会添加到 examples

**建议**：先测试新结构，确认无误后再删除旧文件。

## 📚 下一步

1. ✅ 阅读 `README_NEW.md` 了解新结构
2. ✅ 运行 `examples/` 中的示例
3. ✅ 查看 `docs/SKILLS_GUIDE.md` 学习添加技能
4. ✅ 在 `src/skills/` 中添加你的自定义技能

祝你使用愉快！🎉
