"""
LangChain 智能代理交互式选择器
从 definitions 文件夹动态加载预定义的 Agent
"""
from dotenv import load_dotenv
from src.agents.loader import AgentLoader

# 加载环境变量
load_dotenv()


def display_agents():
    """显示所有可用的 Agent"""
    # 从 definitions 文件夹加载所有 Agent
    agents = AgentLoader.load_all_agents()
    
    print("\n" + "=" * 70)
    print("🤖  可用的 Agent 列表")
    print("=" * 70)
    
    for key, agent_info in agents.items():
        print(f"\n{agent_info['icon']}  [{key}] {agent_info['name']}")
        print(f"    {agent_info['description']}")
        print(f"    版本: {agent_info['version']} | 作者: {agent_info['author']}")
    
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
    
    # 使用 AgentLoader 创建 Agent
    agent = AgentLoader.create_agent_by_choice(choice)
    
    print("-" * 70)
    return agent


def chat_loop(agent, agent_info):
    """对话循环"""
    print(f"\n💬 开始与 {agent_info['name']} 对话")
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
        # 显示 Agent 列表（从 definitions 文件夹动态加载）
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
        
        # 获取 Agent 信息
        agent_info = AgentLoader.get_agent_info_by_choice(choice)
        
        # 进入对话循环
        result = chat_loop(agent, agent_info)
        
        if result == 'quit':
            print("\n👋 再见！")
            break


if __name__ == "__main__":
    main()
