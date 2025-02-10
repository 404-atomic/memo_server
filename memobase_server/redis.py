# 导入Redis客户端类
from redis import Redis
from .core.config import settings

# 创建Redis客户端实例
# 使用配置文件中的设置初始化连接
redis_client = Redis(
    host=settings.REDIS_HOST,      # Redis服务器地址（默认：localhost）
    port=settings.REDIS_PORT,      # Redis端口（默认：6379）
    db=settings.REDIS_DB,          # Redis数据库编号（默认：0）
    password=settings.REDIS_PASSWORD,  # Redis密码（从配置中获取）
    decode_responses=True          # 自动将字节响应解码为字符串，方便处理
)

# 创建Redis连接依赖
# 这个函数将被FastAPI的依赖注入系统使用
async def get_redis():
    """
    获取Redis客户端的依赖函数
    用于FastAPI的依赖注入系统
    使用方法：
    async def some_route(redis: Redis = Depends(get_redis)):
        value = redis.get('some_key')
    """
    return redis_client  # 返回已配置的Redis客户端实例

# 使用示例：
# 1. 设置键值对：redis_client.set('key', 'value', ex=3600)  # ex为过期时间（秒）
# 2. 获取值：value = redis_client.get('key')
# 3. 删除键：redis_client.delete('key')
# 4. 检查键是否存在：exists = redis_client.exists('key') 