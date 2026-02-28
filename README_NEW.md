# LangChain 智能代理项目

一个模块化、可扩展的 LangChain 代理框架，支持多种模型和自定义技能。

## 📁 项目结构

```
line/
├── src/                      # 源代码目录
│   ├── __init__.py
│   ├── config.py            # 配置管理
│   ├── agents/              # 代理模块
│   │   ├── __init__.py
│   │   └── agent_factory.py # 代理工厂
│   ├── skills/              # 技能模块
│   │   ├── __init__.py
│   │   ├── basic_skills.py  # 基础技能
│   │   └── advanced_skills.py # 高级技能
│   └── utils/               # 工具模块
│       ├── __init__.py
│       └── helpers.py       # 辅助函数
│
├── examples/                # 示例代码
│   ├── 01_basic_agent.py   # 基础代理示例
│   ├── 02_advanced_agent.py # 高级代理示例
│   └── 03_custom_agent.py  # 自定义代理示例
│
├── docs/                    # 文档目录
│   └── SKILLS_GUIDE.md     # 技能扩展指南
│
├── config/                  # 配置文件
│   └── .env                # 环境变量
│
├── main_new.py             # 新版主程序
├── requirements.txt        # 项目依赖
└── README.md              # 项目说明
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制并编辑 `.env` 文件：

```bash
# 配置 DeepSeek API Key（推荐）
DEEPSEEK_API_KEY=your_key_here
MODEL_PROVIDER=deepseek
```

### 3. 运行示例

```bash
# 新版主程序
python main_new.py

# 基础代理示例
python examples/01_basic_agent.py

# 高级代理示例
python examples/02_advanced_agent.py

# 自定义代理示例
python examples/03_custom_agent.py
```

## 📚 核心模块

### 1. 配置管理 (`src/config.py`)

统一管理所有配置：

```python
from src.config import config

# 获取当前模型配置
model_config = config.get_model_config()

# 切换模型
config.MODEL_PROVIDER = "openai"
```

### 2. 代理工厂 (`src/agents/agent_factory.py`)

快速创建不同类型的代理：

```python
from src.agents import AgentFactory

# 创建基础代理
agent = AgentFactory.create_basic_agent()

# 创建高级代理
agent = AgentFactory.create_advanced_agent()

# 创建自定义代理
agent = AgentFactory.create_custom_agent(
    tools=[skill1, skill2],
    system_prompt="你的提示词"
)
```

### 3. 技能模块 (`src/skills/`)

所有技能集中管理：

```python
from src.skills import BASIC_SKILLS, ADVANCED_SKILLS, get_all_skills

# 使用基础技能
tools = BASIC_SKILLS

# 使用所有技能
tools = get_all_skills()
```

### 4. 工具函数 (`src/utils/`)

常用辅助函数：

```python
from src.utils import print_header, extract_response

print_header("标题")
text = extract_response(response)
```

## 🛠️ 添加新技能

### 方法1：添加到现有模块

编辑 `src/skills/basic_skills.py` 或 `advanced_skills.py`：

```python
def my_new_skill(param: str) -> str:
    """技能描述"""
    return f"结果: {param}"

# 添加到导出列表
BASIC_SKILLS = [
    get_weather,
    calculate,
    my_new_skill,  # 新技能
]
```

### 方法2：创建新的技能模块

创建 `src/skills/my_skills.py`：

```python
def skill1(x: str) -> str:
    """技能1"""
    return f"处理 {x}"

MY_SKILLS = [skill1]
```

在 `src/skills/__init__.py` 中导入：

```python
from .my_skills import MY_SKILLS
```

## 🎯 使用模式

### 模式1：快速原型

```python
from src.agents import AgentFactory

agent = AgentFactory.create_basic_agent()
response = agent.invoke({"messages": [{"role": "user", "content": "你好"}]})
```

### 模式2：生产环境

```python
from src.agents import AgentFactory
from src.config import config
from src.utils import extract_response

# 配置
config.MODEL_PROVIDER = "deepseek"

# 创建
agent = AgentFactory.create_advanced_agent()

# 使用
response = agent.invoke({"messages": [{"role": "user", "content": "查询"}]})
result = extract_response(response)
```

### 模式3：高度自定义

```python
from src.agents import AgentFactory
from src.skills import BASIC_SKILLS

def custom_skill(x: str) -> str:
    return f"自定义: {x}"

agent = AgentFactory.create_custom_agent(
    tools=BASIC_SKILLS + [custom_skill],
    system_prompt="自定义提示词"
)
```

## 📖 文档

- [技能扩展指南](docs/SKILLS_GUIDE.md) - 详细的技能开发教程
- [示例代码](examples/) - 各种使用示例

## 🔧 支持的模型

- **DeepSeek** (推荐) - 性价比最高
- **Anthropic Claude** - 强大的推理能力
- **OpenAI GPT** - 经典选择
- **Google Gemini** - 多模态支持

切换模型只需修改 `.env` 中的 `MODEL_PROVIDER`。

## 💡 最佳实践

1. **模块化开发** - 将技能按功能分类到不同模块
2. **统一管理** - 使用工厂模式创建代理
3. **配置分离** - 环境变量和代码分离
4. **复用代码** - 使用公共工具函数
5. **清晰文档** - 为每个技能添加 docstring

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
