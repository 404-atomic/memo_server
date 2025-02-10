# redis.py Redis配置说明

## 代码详解

### 导入部分

主要导入以下组件：
- `Redis`: Redis客户端类，用于创建与Redis服务器的连接
- `settings`: 我们之前创建的配置对象，包含Redis相关配置

### Redis客户端配置
```python
redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True
)
```

参数说明：
- `host`: Redis服务器地址（我们设置为localhost）
- `port`: Redis端口（我们设置为6379）
- `db`: Redis数据库编号（我们设置为0）
- `password`: Redis密码（我们设置为'atomic'）
- `decode_responses=True`: 自动将Redis的字节响应解码为Python字符串

### 依赖函数
```python
async def get_redis():
    return redis_client
```
- 这是一个异步函数，用于FastAPI的依赖注入系统
- 返回已配置的Redis客户端实例
- 后续可以在API路由中使用这个依赖来获取Redis客户端

## 使用示例

### 基本操作
```python
# 存储数据
redis_client.set('key', 'value')
redis_client.setex('key', 3600, 'value')  # 设置过期时间（3600秒）

# 获取数据
value = redis_client.get('key')

# 删除数据
redis_client.delete('key')

# 检查键是否存在
exists = redis_client.exists('key')
```

## Redis服务配置

### Windows环境配置

1. 检查Redis服务状态：
```bash
net start Redis
```

2. 使用Redis CLI测试连接：
```bash
redis-cli
auth atomic
ping
```
- 如果返回"PONG"，说明连接成功

3. 重新设置Redis密码（如需要）：
```bash
redis-cli
config set requirepass atomic
``` 