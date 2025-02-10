from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """用户基本信息模式：定义用户的基本属性"""
    
    # EmailStr类型会自动验证邮箱格式
    # 例如：user@example.com
    email: EmailStr
    
    # 用户全名，字符串类型
    # 例如：张三
    full_name: str

class UserCreate(UserBase):
    """创建用户的请求模式：继承基本信息，添加密码字段"""
    
    # 密码字段，仅用于用户创建
    # 注意：这是明文密码，将在API层进行加密
    password: str

class UserResponse(UserBase):
    """用户信息响应模式：用于向客户端返回用户信息"""
    
    # 用户ID，整数类型
    id: int
    
    # 创建时间，datetime类型
    # 包含时区信息
    created_at: datetime
    
    # 更新时间，可选字段
    # 新用户的更新时间为空
    updated_at: Optional[datetime] = None

    @property
    def formatted_created_at(self) -> str:
        return self.created_at.strftime("%Y-%m-%d %I:%M %p")

    class Config:
        # 允许从ORM模型创建
        # 用于将SQLAlchemy模型转换为API响应
        from_attributes = True
        
        # 示例数据，用于API文档
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "full_name": "张三",
                "id": 1,
                "created_at": "2024-02-10T10:00:00",
                "updated_at": None
            }
        } 