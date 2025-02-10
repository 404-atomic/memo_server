from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ....database import get_db
from ....schemas.user import UserCreate, UserResponse
from ....models.user import User
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    创建新用户
    
    参数：
    - user: 用户创建请求数据
    - db: 数据库会话（通过依赖注入获取）
    
    返回：
    - 创建成功的用户信息（不包含密码）
    """
    hashed_password = pwd_context.hash(user.password)
    
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    获取指定用户信息
    
    参数：
    - user_id: 用户ID（路径参数）
    - db: 数据库会话
    
    返回：
    - 用户信息
    - 如果用户不存在，返回404错误
    """
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserResponse])
async def read_users(
    skip: int = 0,  # 跳过的记录数
    limit: int = 100,  # 返回的最大记录数
    db: AsyncSession = Depends(get_db)
):
    """
    获取用户列表
    
    参数：
    - skip: 跳过前面的记录数（分页用）
    - limit: 返回的最大记录数（分页用）
    - db: 数据库会话
    
    返回：
    - 用户列表
    """
    # Get list of users
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users 