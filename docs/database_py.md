# database.py 数据库配置说明

## 代码详解

### 导入部分

主要导入以下组件：
- `create_async_engine`: 创建异步SQL引擎
- `AsyncSession`: 异步会话类
- `declarative_base`: 用于创建ORM模型的基类
- `sessionmaker`: 创建会话工厂
- `settings`: 我们之前创建的配置对象

### URL转换
```python
db_url = str(settings.DATABASE_URL)
async_db_url = db_url.replace('postgresql://', 'postgresql+asyncpg://')
```
- 将普通PostgreSQL URL转换为支持异步的格式
- `asyncpg` 是PostgreSQL的异步驱动程序

### 创建引擎
```python
engine = create_async_engine(async_db_url, echo=settings.DEBUG)
```
- 创建异步数据库引擎
- `echo=settings.DEBUG` 在调试模式下会打印SQL语句

### 创建会话工厂
```python
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
```
- 创建用于生成数据库会话的工厂
- `expire_on_commit=False` 防止提交后对象被过期

### 创建基类
```python
Base = declarative_base()
```
- 创建ORM模型的基类
- 后续所有的数据模型都会继承这个基类

### 会话依赖函数
```python
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```
- 这是一个异步生成器函数
- 用于FastAPI的依赖注入系统
- 自动处理会话的提交和回滚
- 使用上下文管理器确保会话正确关闭

## 安装依赖

在使用这个文件之前，我们需要确保已经安装了asyncpg：
```bash
pip install asyncpg
```

## 主要作用

该文件的主要作用是：
- 建立与数据库的异步连接
- 提供会话管理
- 提供ORM基类
- 处理事务的提交和回滚 