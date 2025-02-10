# schemas/user.py 用户模式说明

## 代码详解

### 导入部分

主要导入以下组件：
- `Optional`: 用于定义可选字段
- `datetime`: 日期时间类型
- `BaseModel`: Pydantic基础模型类
- `EmailStr`: 用于邮箱验证的特殊字符串类型

### 模式类定义

#### UserBase（基础模式）
```python
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
```
- 定义用户的基本信息
- `email`: 使用`EmailStr`确保邮箱格式正确
- `full_name`: 用户全名

#### UserCreate（创建请求模式）
```python
class UserCreate(UserBase):
    password: str
```
- 继承自`UserBase`
- 添加`password`字段用于用户创建
- 用于处理用户注册请求

#### UserResponse（响应模式）
```python
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
```
- 继承自`UserBase`
- 添加数据库模型特有的字段
- `id`: 用户ID
- `created_at`: 创建时间
- `updated_at`: 更新时间（可选）
- `from_attributes = True`: 允许从ORM模型创建

## 使用说明

这些模式用于：
- 验证API请求数据
- 序列化API响应数据
- 在API层和数据库层之间转换数据

### 使用示例
```python
# 创建用户请求
user_data = UserCreate(
    email="user@example.com",
    full_name="Test User",
    password="secret123"
)

# API响应
user_response = UserResponse(
    id=1,
    email="user@example.com",
    full_name="Test User",
    created_at=datetime.now(),
    updated_at=None
) 