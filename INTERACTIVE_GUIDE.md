# 🤖 交互式 Agent 选择器使用指南

## 📋 功能说明

这个交互式程序允许你在启动后选择不同的 Agent 进行对话。

## 🎯 可用的 Agent 类型

### 1️⃣ 基础 Agent (Basic Agent)
- **技能**: 天气查询、计算器、搜索
- **适用场景**: 日常简单查询和计算
- **示例问题**:
  - "北京今天天气怎么样？"
  - "计算 123 * 456"
  - "搜索 Python 教程"

### 2️⃣ 高级 Agent (Advanced Agent)
- **技能**: 全部技能（基础 + 时间管理 + 数据处理）
- **适用场景**: 需要更多功能的复杂任务
- **示例问题**:
  - "现在几点了？"
  - "帮我创建一个提醒"
  - "格式化这些数据"

### 3️⃣ 自定义 Agent (Custom Agent)
- **技能**: 可自定义技能集
- **适用场景**: 特定领域的专业任务
- **特点**: 灵活配置，按需定制

## 🚀 启动方式

### 方式 1: 使用启动脚本（推荐）
```bash
./run_interactive.sh
```

### 方式 2: 直接运行 Python
```bash
python3 main.py
```

## 💡 使用流程

1. **启动程序** - 运行上述命令之一
2. **查看 Agent 列表** - 程序会显示所有可用的 Agent
3. **选择 Agent** - 输入对应的数字 (1-3)
4. **开始对话** - 与选中的 Agent 进行交互
5. **切换或退出**:
   - 输入 `back` - 返回 Agent 选择菜单
   - 输入 `quit` 或 `q` - 退出程序

## 📝 示例对话流程

```
======================================================================
🎯  欢迎使用 LangChain 智能代理交互系统
======================================================================

======================================================================
🤖  可用的 Agent 列表
======================================================================

🔷  [1] 基础 Agent
    拥有基础技能：天气查询、计算器、搜索

💎  [2] 高级 Agent
    拥有全部技能：基础功能 + 时间管理 + 数据处理

⚙️  [3] 自定义 Agent
    可自定义技能和提示词的灵活 Agent

======================================================================

请选择 Agent (1-3) 或输入 'q' 退出: 1

----------------------------------------------------------------------
🤖 创建基础代理
📋 模型: Claude Sonnet 4.5
🛠️  技能: 天气查询、计算器、搜索
----------------------------------------------------------------------

💬 开始与 基础 Agent 对话
提示: 输入 'back' 返回 Agent 选择，输入 'quit' 退出程序

👤 你: 北京天气怎么样？

🤖 助手: 北京今天多云，温度 15°C

👤 你: back

🔙 返回 Agent 选择...
```

## ⚙️ 环境配置

确保 `.env` 文件中已配置相应的 API 密钥：

```env
# 选择模型提供商
MODEL_PROVIDER=anthropic  # 可选: anthropic, openai, google, deepseek

# API 密钥
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here
```

## 🛠️ 自定义 Agent

你可以在 `main.py` 中的 `create_selected_agent()` 函数里修改自定义 Agent 的配置：

```python
elif choice == "3":
    from src.skills import BASIC_SKILLS, ADVANCED_SKILLS
    
    # 自定义技能组合
    custom_tools = BASIC_SKILLS + ADVANCED_SKILLS[:2]
    
    agent = AgentFactory.create_custom_agent(
        tools=custom_tools,
        system_prompt="你的自定义提示词"
    )
```

## 🎨 添加更多 Agent

如果想添加更多 Agent 类型，只需在 `display_agents()` 函数中添加新项：

```python
"4": {
    "name": "专家 Agent",
    "description": "专注于某个特定领域的专家",
    "icon": "🎓"
}
```

然后在 `create_selected_agent()` 中添加对应的创建逻辑：

```python
elif choice == "4":
    agent = AgentFactory.create_expert_agent()
```

## ❓ 常见问题

**Q: 如何切换到另一个 Agent？**  
A: 在对话中输入 `back` 即可返回选择菜单

**Q: 可以同时使用多个 Agent 吗？**  
A: 当前版本一次只能使用一个 Agent，但可以随时切换

**Q: 如何退出程序？**  
A: 在任何时候输入 `quit`、`exit` 或 `q` 即可退出

## 📚 相关文件

- `main.py` - 主程序文件
- `src/agents/agent_factory.py` - Agent 工厂类
- `src/skills/` - 技能模块
- `.env` - 环境变量配置

## 🎯 下一步

- 尝试所有 3 种 Agent，感受不同的能力
- 根据需求自定义 Agent 的技能组合
- 添加更多自定义的 Agent 类型
- 为 Agent 添加更多工具和技能

祝你使用愉快！🚀
