# 导入SQLAlchemy所需组件
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base

class User(Base):
    """用户数据模型：定义用户在数据库中的存储结构"""
    
    __tablename__ = "users"  # 指定数据库表名
    
    # 用户ID：主键，自动递增
    # primary_key=True：设置为主键
    # index=True：创建索引，提高查询性能
    id = Column(Integer, primary_key=True, index=True)
    
    # 用户邮箱：唯一值，带索引
    # unique=True：确保邮箱不重复
    # index=True：创建索引，加快邮箱查询
    email = Column(String, unique=True, index=True)
    
    # 用户全名：存储用户的完整姓名
    # String类型，可以存储任意长度的字符串
    full_name = Column(String)
    
    # 加密后的密码
    # 注意：永远不要存储明文密码
    # 使用passlib进行密码加密
    hashed_password = Column(String)
    
    # 创建时间：自动设置为当前时间
    # timezone=True：包含时区信息
    # server_default：在数据库层面设置默认值
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),  # 使用数据库的now()函数
        nullable=False  # 不允许为空
    )
    
    # 更新时间：在记录更新时自动更新
    # onupdate：当记录更新时自动设置为当前时间
    # nullable=True：允许为空（新创建的用户尚未更新）
    updated_at = Column(
        DateTime(timezone=True), 
        onupdate=func.now(),  # 在更新时自动设置为当前时间
        nullable=True  # 允许为空
    )

    # 可以添加其他方法，例如：
    # def verify_password(self, password: str) -> bool:
    #     return pwd_context.verify(password, self.hashed_password) 