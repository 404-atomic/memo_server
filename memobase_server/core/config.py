from typing import Any, Dict, Optional 
from pydantic import PostgresDsn, validator  
from pydantic_settings import BaseSettings 
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# 创建配置类
class Settings(BaseSettings):
    # API版本配置
    API_VERSION: str = "v1"  # 默认API版本为v1
    API_PREFIX: str = f"/api/{API_VERSION}"  # API前缀路径，例如：/api/v1
    
    # 调试模式配置
    DEBUG: bool = False  # 默认关闭调试模式
    
    # 数据库配置
    DATABASE_URL: PostgresDsn  # PostgreSQL数据库连接URL，使用PostgresDsn类型确保URL格式正确
    
    # Redis配置
    REDIS_HOST: str = "localhost"  # Redis服务器地址，默认为localhost
    REDIS_PORT: int = 6379        # Redis端口，默认为6379
    REDIS_DB: int = 0            # Redis数据库编号，默认为0
    REDIS_PASSWORD: str          # Redis密码
    
    # 安全配置
    SECRET_KEY: str              # 用于JWT token加密的密钥
    ALGORITHM: str = "HS256"     # JWT加密算法，默认为HS256
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # token过期时间，默认30分钟
    
    # 配置类设置
    class Config:
        case_sensitive = True    # 大小写敏感
        env_file = ".env"       # 指定环境变量文件路径

# 创建settings实例
settings = Settings()