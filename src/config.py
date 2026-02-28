"""
配置管理模块
"""
import os
from typing import Optional
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class Config:
    """全局配置类"""
    
    # 模型配置
    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "deepseek")
    
    # API Keys
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # 模型映射
    MODEL_MAP = {
        "deepseek": {
            "model": "openai:deepseek-chat",
            "name": "DeepSeek V3",
            "base_url": "https://api.deepseek.com",
        },
        "anthropic": {
            "model": "anthropic:claude-sonnet-4-5",
            "name": "Anthropic Claude Sonnet 4.5",
        },
        "openai": {
            "model": "openai:gpt-4o",
            "name": "OpenAI GPT-4o",
        },
        "google": {
            "model": "google:gemini-2.0-flash-exp",
            "name": "Google Gemini 2.0 Flash",
        },
    }
    
    @classmethod
    def get_model_config(cls, provider: Optional[str] = None):
        """获取模型配置"""
        provider = provider or cls.MODEL_PROVIDER
        return cls.MODEL_MAP.get(provider, cls.MODEL_MAP["deepseek"])
    
    @classmethod
    def setup_deepseek(cls):
        """配置 DeepSeek 环境"""
        if cls.DEEPSEEK_API_KEY:
            os.environ["OPENAI_API_KEY"] = cls.DEEPSEEK_API_KEY
            os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"


# 导出配置实例
config = Config()
