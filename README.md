# 🤖 LangChain 智能代理项目

一个模块化、可扩展的 LangChain 代理框架，支持动态加载 Agent、多种模型和自定义技能。

## ✨ 主要特性

- 🎯 **动态 Agent 加载** - 从配置文件夹自动加载预定义的 Agent
- 🔄 **交互式选择** - 启动后可选择不同的 Agent 进行对话
- 🛠️ **模块化设计** - Agent、Skills、Config 完全分离
- 🎨 **易于扩展** - 添加新 Agent 只需创建定义文件
- 🌐 **多模型支持** - 支持 Anthropic、OpenAI、Google、DeepSeek
- 📦 **开箱即用** - 预定义了基础、高级、自定义 3 种 Agent

## 📁 项目结构

```
line/
├── src/
│   ├── agents/                      # Agent 模块
│   │   ├── __init__.py
│   │   ├── agent_factory.py        # Agent 工厂（旧版兼容）
│   │   ├── loader.py               # 🆕 Agent 加载器
│   │   └── definitions/            # 🆕 Agent 定义文件夹
│   │       ├── __init__.py         # Agent 注册中心
│   │       ├── _template.py        # Agent 模板
│   │       ├── HOW_TO_ADD_AGENT.md # 添加指南
│   │       ├── basic_agent.py      # 基础 Agent
│   │       ├── advanced_agent.py   # 高级 Agent
│   │       └── custom_agent.py     # 自定义 Agent
│   │
│   ├── skills/                      # 技能模块
│   │   ├── __init__.py
│   │   ├── basic_skills.py         # 基础技能
│   │   └── advanced_skills.py      # 高级技能
│   │
│   ├── utils/                       # 工具模块
│   └── config.py                    # 配置管理
│
├── examples/                        # 示例代码
│   ├── 01_basic_agent.py
│   ├── 02_advanced_agent.py
│   └── 03_custom_agent.py
│
├── docs/                            # 文档
│   └── SKILLS_GUIDE.md
│
├── main.py                          # 🔄 交互式主程序
├── run_interactive.sh               # 启动脚本
├── INTERACTIVE_GUIDE.md             # 使用指南
├── PROJECT_STRUCTURE.md             # 架构说明
├── requirements.txt                 # 依赖
└── .env                            # 环境变量

```

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/tarol/agents.git
cd agents
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并填入 API 密钥：

```bash
cp .env.example .env
```

编辑 `.env`：

```env
# 选择模型提供商
MODEL_PROVIDER=anthropic  # 可选: anthropic, openai, google, deepseek

# API 密钥（至少配置一个）
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_key_here
DEEPSEEK_API_KEY=your_deepseek_key_here
```

### 4. 启动程序

**方式 1：使用启动脚本（推荐）**
```bash
./run_interactive.sh
```

**方式 2：直接运行**
```bash
python main.py
```

## 🎮 使用方式

### 交互式模式

启动后会显示所有可用的 Agent：

```
======================================================================
🤖  可用的 Agent 列表
======================================================================

🔷  [1] 基础 Agent
    拥有基础技能：天气查询、计算器、搜索
    版本: 1.0.0 | 作者: System

💎  [2] 高级 Agent
    拥有全部技能：基础功能 + 时间管理 + 数据处理
    版本: 1.0.0 | 作者: System

⚙️  [3] 自定义 Agent
    专注于天气和计算的精简助手
    版本: 1.0.0 | 作者: User

======================================================================

请选择 Agent (1-3) 或输入 'q' 退出:
```

选择后即可开始对话：
- 输入 `back` - 返回 Agent 选择
- 输入 `quit` - 退出程序

### 编程方式

```python
from src.agents.loader import AgentLoader

# 方式1: 通过 ID 创建
agent = AgentLoader.create_agent_by_id("basic")

# 方式2: 通过选择创建
agent = AgentLoader.create_agent_by_choice("1")

# 获取所有 Agent 信息
agents = AgentLoader.load_all_agents()
for key, info in agents.items():
    print(f"{info['icon']} {info['name']}")

# 使用 Agent
response = agent.invoke({
    "messages": [{"role": "user", "content": "你好"}]
})
```

## 🎨 添加自定义 Agent

### 3 步添加新 Agent

**步骤 1：创建定义文件**

```bash
cd src/agents/definitions/
cp _template.py my_expert_agent.py
```

**步骤 2：编辑 Agent 定义**

```python
# my_expert_agent.py
from ...skills import BASIC_SKILLS, ADVANCED_SKILLS

AGENT_INFO = {
    "id": "expert",
    "name": "专家 Agent",
    "description": "领域专家级智能助手",
    "icon": "🎓",
    "version": "1.0.0",
    "author": "Your Name",
}

AGENT_CONFIG = {
    "tools": BASIC_SKILLS + ADVANCED_SKILLS,
    "system_prompt": """你是一个专业的领域专家...""",
}

def get_agent_info():
    return AGENT_INFO

def get_agent_config():
    return AGENT_CONFIG
```

**步骤 3：注册 Agent**

编辑 `src/agents/definitions/__init__.py`：

```python
from . import my_expert_agent  # 添加导入

AVAILABLE_AGENTS = [
    basic_agent,
    advanced_agent,
    custom_agent,
    my_expert_agent,  # 添加到列表
]
```

完成！运行 `python main.py` 即可看到新 Agent。

📚 详细说明见：[如何添加 Agent](src/agents/definitions/HOW_TO_ADD_AGENT.md)

## 📖 可用的 Agent

| Agent | 图标 | 技能 | 适用场景 |
|-------|------|------|----------|
| 基础 Agent | 🔷 | 天气、计算、搜索 | 日常简单查询 |
| 高级 Agent | 💎 | 全部技能 | 复杂多样任务 |
| 自定义 Agent | ⚙️ | 天气、计算 | 特定领域 |

## 🛠️ 技能系统

### 基础技能 (BASIC_SKILLS)

- 🌤️ **天气查询** - 获取城市天气信息
- 🔢 **计算器** - 数学表达式计算
- 🔍 **搜索** - 信息检索（模拟）

### 高级技能 (ADVANCED_SKILLS)

- ⏰ **时间** - 获取当前时间
- 📝 **提醒** - 创建提醒事项
- 📊 **数据格式化** - JSON/数据处理

### 添加自定义技能

参考 [技能扩展指南](docs/SKILLS_GUIDE.md)

## 🌐 支持的模型

| 提供商 | 模型 | 环境变量 |
|--------|------|----------|
| Anthropic | Claude Sonnet 4.5 | `ANTHROPIC_API_KEY` |
| OpenAI | GPT-4o | `OPENAI_API_KEY` |
| Google | Gemini 2.0 Flash | `GOOGLE_API_KEY` |
| DeepSeek | DeepSeek Chat | `DEEPSEEK_API_KEY` |

切换模型：修改 `.env` 中的 `MODEL_PROVIDER`

## 📚 文档

- [交互式使用指南](INTERACTIVE_GUIDE.md) - 详细的使用说明
- [项目架构说明](PROJECT_STRUCTURE.md) - 代码结构和设计
- [添加 Agent 指南](src/agents/definitions/HOW_TO_ADD_AGENT.md) - 如何创建新 Agent
- [技能扩展指南](docs/SKILLS_GUIDE.md) - 如何添加新技能

## 🎯 核心优势

### 🔧 动态架构

```
旧版本（硬编码）              新版本（动态加载）
-----------------            ------------------
main.py                      main.py
  └─ if choice == "1"          └─ AgentLoader
       create Agent 1             └─ definitions/
     elif choice == "2"               ├─ agent1.py
       create Agent 2                 ├─ agent2.py
     elif choice == "3"               └─ agent3.py
       create Agent 3
```

### ✨ 主要改进

| 特性 | 旧版本 | 新版本 |
|------|--------|--------|
| Agent 定义 | 硬编码 | 独立配置文件 |
| 添加 Agent | 修改多处代码 | 添加一个文件 |
| 元数据 | 简单字典 | 完整信息 |
| 可维护性 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| 扩展性 | ⭐⭐ | ⭐⭐⭐⭐⭐ |

## 🔄 示例代码

查看 `examples/` 文件夹：

- `01_basic_agent.py` - 基础 Agent 使用
- `02_advanced_agent.py` - 高级 Agent 使用
- `03_custom_agent.py` - 自定义 Agent 创建

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可

MIT License

## 🔗 相关链接

- [LangChain 文档](https://python.langchain.com/)
- [GitHub 仓库](https://github.com/tarol/agents)

---

⭐ 如果这个项目对你有帮助，请给个 Star！
