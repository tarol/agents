"""
LangChain 智能代理交互式选择器
这个示例展示了如何让用户选择不同的 Agent 进行对话
"""
from dotenv import load_dotenv
from src.agents.agent_factory import AgentFactory

# 加载环境变量
load_dotenv()


def display_agents():
    """显示所有可用的 Agent"""
    agents = {
        "1": {
            "name": "基础 Agent",
            "description": "拥有基础技能：天气查询、计算器、搜索",
            "icon": "🔷"
        },
        "2": {
            "name": "高级 Agent",
            "description": "拥有全部技能：基础功能 + 时间管理 + 数据处理",
            "icon": "💎"
        },
        "3": {
            "name": "自定义 Agent",
            "description": "可自定义技能和提示词的灵活 Agent",
            "icon": "⚙️"
        }
    }
    
    print("\n" + "=" * 70)
    print("🤖  可用的 Agent 列表")
    print("=" * 70)
    
    for key, agent_info in agents.items():
        print(f"\n{agent_info['icon']}  [{key}] {agent_info['name']}")
        print(f"    {agent_info['description']}")
    
    print("\n" + "=" * 70)
    return agents


def get_user_choice(agents):
    """获取用户选择"""
    while True:
        choice = input(f"\n请选择 Agent (1-{len(agents)}) 或输入 'q' 退出: ").strip()
        
        if choice.lower() == 'q':
            return None
        
        if choice in agents:
            return choice
        
        print("❌ 无效选择，请重新输入！")


def create_selected_agent(choice):
    """根据用户选择创建 Agent"""
    print("\n" + "-" * 70)
    
    if choice == "1":
        agent = AgentFactory.create_basic_agent()
    elif choice == "2":
        agent = AgentFactory.create_advanced_agent()
    elif choice == "3":
        # 自定义 Agent 示例
        from src.skills import BASIC_SKILLS
        agent = AgentFactory.create_custom_agent(
            tools=BASIC_SKILLS[:2],  # 只使用前两个技能
            system_prompt="你是一个专注于天气和计算的助手。"
        )
    else:
        return None
    
    print("-" * 70)
    return agent


def chat_loop(agent, agent_name):
    """对话循环"""
    print(f"\n💬 开始与 {agent_name} 对话")
    print("提示: 输入 'back' 返回 Agent 选择，输入 'quit' 退出程序\n")
    
    while True:
        user_input = input("👤 你: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == 'back':
            print("\n🔙 返回 Agent 选择...")
            return 'back'
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            return 'quit'
        
        try:
            print("\n🤖 助手: ", end="", flush=True)
            response = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            print(response)
            print()
        except Exception as e:
            print(f"\n❌ 错误: {str(e)}\n")


def main():
    """主函数"""
    print("\n" + "=" * 70)
    print("🎯  欢迎使用 LangChain 智能代理交互系统")
    print("=" * 70)
    
    while True:
        # 显示 Agent 列表
        agents = display_agents()
        
        # 获取用户选择
        choice = get_user_choice(agents)
        
        if choice is None:
            print("\n👋 再见！")
            break
        
        # 创建选中的 Agent
        agent = create_selected_agent(choice)
        
        if agent is None:
            print("❌ Agent 创建失败！")
            continue
        
        # 进入对话循环
        result = chat_loop(agent, agents[choice]['name'])
        
        if result == 'quit':
            print("\n👋 再见！")
            break


if __name__ == "__main__":
    main()
