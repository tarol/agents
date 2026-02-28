"""
Agent 加载器
从 definitions 文件夹动态加载和创建 Agent
"""
from langchain.agents import create_agent
from ..config import config
from .definitions import get_all_agent_definitions, get_agent_by_id


class AgentLoader:
    """Agent 加载器类"""
    
    @staticmethod
    def load_all_agents():
        """加载所有可用的 Agent 信息
        
        Returns:
            字典，键为序号，值为 Agent 信息
        """
        agent_definitions = get_all_agent_definitions()
        agents = {}
        
        for idx, agent_module in enumerate(agent_definitions, 1):
            info = agent_module.get_agent_info()
            agents[str(idx)] = info
        
        return agents
    
    @staticmethod
    def create_agent_by_choice(choice: str):
        """根据用户选择创建 Agent
        
        Args:
            choice: 用户选择的序号（字符串）
            
        Returns:
            创建的 Agent 实例，失败返回 None
        """
        agent_definitions = get_all_agent_definitions()
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(agent_definitions):
                agent_module = agent_definitions[idx]
                return AgentLoader._create_agent_from_definition(agent_module)
        except (ValueError, IndexError):
            pass
        
        return None
    
    @staticmethod
    def create_agent_by_id(agent_id: str):
        """根据 Agent ID 创建 Agent
        
        Args:
            agent_id: Agent 的唯一标识符
            
        Returns:
            创建的 Agent 实例，失败返回 None
        """
        agent_module = get_agent_by_id(agent_id)
        if agent_module:
            return AgentLoader._create_agent_from_definition(agent_module)
        return None
    
    @staticmethod
    def _create_agent_from_definition(agent_module):
        """从定义模块创建 Agent
        
        Args:
            agent_module: Agent 定义模块
            
        Returns:
            创建的 Agent 实例
        """
        info = agent_module.get_agent_info()
        config_data = agent_module.get_agent_config()
        
        # 获取模型配置
        model_config = config.get_model_config()
        
        # 配置 DeepSeek
        if config.MODEL_PROVIDER == "deepseek":
            config.setup_deepseek()
        
        # 打印创建信息
        print(f"🤖 创建 {info['name']}")
        print(f"📋 模型: {model_config['name']}")
        print(f"🛠️  技能数量: {len(config_data['tools'])}")
        print(f"📝 版本: {info['version']}")
        print()
        
        # 创建 Agent
        agent = create_agent(
            model=model_config["model"],
            tools=config_data["tools"],
            system_prompt=config_data["system_prompt"],
        )
        
        return agent
    
    @staticmethod
    def get_agent_info_by_choice(choice: str):
        """根据选择获取 Agent 信息
        
        Args:
            choice: 用户选择的序号（字符串）
            
        Returns:
            Agent 信息字典，失败返回 None
        """
        agents = AgentLoader.load_all_agents()
        return agents.get(choice)
