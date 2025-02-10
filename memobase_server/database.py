# 导入所需的SQLAlchemy组件
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from .core.config import settings

# 将PostgreSQL URL转换为异步格式
# 例如：postgresql://user:pass@localhost/db 转换为 postgresql+asyncpg://user:pass@localhost/db
db_url = str(settings.DATABASE_URL)
async_db_url = db_url.replace('postgresql://', 'postgresql+asyncpg://')

# 创建异步数据库引擎
# echo=settings.DEBUG：在调试模式下打印SQL语句
engine = create_async_engine(
    async_db_url,  # 数据库连接URL
    echo=settings.DEBUG  # 当DEBUG=True时，会打印SQL语句
)

# 创建异步会话工厂
# expire_on_commit=False：防止提交后对象被过期
# class_=AsyncSession：指定使用异步会话类
AsyncSessionLocal = sessionmaker(
    engine,  # 使用上面创建的引擎
    class_=AsyncSession,  # 指定会话类为异步会话
    expire_on_commit=False  # 提交后不过期对象，方便后续操作
)

# 创建声明性基类
# 所有的ORM模型都将继承这个基类
Base = declarative_base()

# 创建数据库会话依赖
# 这个函数将被FastAPI的依赖注入系统使用
async def get_db():
    """
    创建数据库会话的异步上下文管理器
    用于FastAPI的依赖注入系统
    使用方法：
    async def some_route(db: AsyncSession = Depends(get_db)):
        ...
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session  # 提供数据库会话
            await session.commit()  # 如果没有异常，提交事务
        except Exception:
            await session.rollback()  # 如果有异常，回滚事务
            raise  # 重新抛出异常