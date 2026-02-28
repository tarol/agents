"""
代理工厂模块
用于创建不同类型的代理
"""
from langchain.agents import create_agent
from ..config import config
from ..skills import BASIC_SKILLS, ADVANCED_SKILLS, get_all_skills


class AgentFactory:
    """代理工厂类"""
    
    @staticmethod
    def create_basic_agent():
        """创建基础代理（只包含基础技能）"""
        model_config = config.get_model_config()
        
        # 配置 DeepSeek
        if config.MODEL_PROVIDER == "deepseek":
            config.setup_deepseek()
        
        print(f"🤖 创建基础代理")
        print(f"📋 模型: {model_config['name']}")
        print(f"🛠️  技能: 天气查询、计算器、搜索\n")
        
        agent = create_agent(
            model=model_config["model"],
            tools=BASIC_SKILLS,
            system_prompt="""你是一个智能助手，拥有以下基础技能：
            1. 查询天气信息
            2. 进行数学计算
            3. 搜索信息
            
            请根据用户的问题，选择合适的工具来回答。回答要简洁、准确、友好。""",
        )
        
        return agent
    
    @staticmethod
    def create_advanced_agent():
        """创建高级代理（包含所有技能）"""
        model_config = config.get_model_config()
        
        if config.MODEL_PROVIDER == "deepseek":
            config.setup_deepseek()
        
        print(f"🤖 创建高级代理")
        print(f"📋 模型: {model_config['name']}")
        print(f"🛠️  技能: 全部技能\n")
        
        agent = create_agent(
            model=model_config["model"],
            tools=get_all_skills(),
            system_prompt="""你是一个功能强大的智能助手，拥有多种技能：
            
            📊 **基础功能**：天气查询、数学计算、信息搜索
            ⏰ **时间管理**：获取时间、创建提醒
            💾 **数据处理**：格式化数据、文件操作
            
            请根据用户需求，灵活运用这些技能，提供专业、高效的服务。""",
        )
        
        return agent
    
    @staticmethod
    def create_custom_agent(tools: list, system_prompt: str):
        """创建自定义代理
        
        Args:
            tools: 技能列表
            system_prompt: 系统提示词
        
        Returns:
            自定义代理
        """
        model_config = config.get_model_config()
        
        if config.MODEL_PROVIDER == "deepseek":
            config.setup_deepseek()
        
        print(f"🤖 创建自定义代理")
        print(f"📋 模型: {model_config['name']}")
        print(f"🛠️  技能数量: {len(tools)}\n")
        
        agent = create_agent(
            model=model_config["model"],
            tools=tools,
            system_prompt=system_prompt,
        )
        
        return agent
