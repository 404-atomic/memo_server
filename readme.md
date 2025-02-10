# MemoBase 服务端

## 项目概述
MemoBase是一个现代化的备忘录管理系统，使用FastAPI和SQLAlchemy构建。

## 快速开始
查看[快速启动指南](docs/quick_setup.md)了解如何安装和运行项目。

## 技术栈
- FastAPI: 现代化的Python Web框架
- SQLAlchemy: ORM数据库操作
- PostgreSQL: 主数据库
- Redis: 缓存服务
- Pydantic: 数据验证
- Alembic: 数据库迁移工具
- Passlib: 密码加密

## 项目结构
```
memobase_server/
├── api/
│   └── v1/
│       └── endpoints/
│           └── users.py    # 用户API接口
│   ├── api_users.md       # 用户API接口文档
│   └── api_testing.md     # API测试文档
├── core/
│   └── config.py          # 配置管理
├── models/
│   └── user.py            # 数据库模型
├── schemas/
│   └── user.py            # 数据验证模式
├── database.py            # 数据库连接
├── redis.py              # Redis连接
└── main.py              # 主应用入口
migrations/               # 数据库迁移
├── versions/             # 迁移版本文件
│   └── *.py             # 具体迁移脚本
├── env.py               # 迁移环境配置
└── script.py.mako       # 迁移模板
docs/                   # 项目文档
├── config_py.md        # 配置系统说明
├── database_py.md      # 数据库配置说明
├── redis_py.md         # Redis配置说明
├── models_user_py.md   # 用户模型说明
├── schemas_user_py.md  # 数据验证说明
└── migrations.md       # 数据库迁移说明
```

## 开发步骤

### 1. 环境准备
1. 创建Python虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. 安装依赖：
```bash
pip install fastapi sqlalchemy alembic psycopg2-binary redis pydantic[email] python-dotenv passlib[bcrypt] uvicorn
```

### 2. 配置文件设置
1. 创建 `.env` 文件：
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=atomic
SECRET_KEY=your-secret-key
DEBUG=True
```

2. 创建配置管理模块 [core/config.py](docs/config_py.md)
- 实现环境变量加载
- 配置数据库连接
- 设置Redis参数
- 配置API和安全选项

### 3. 数据库配置
1. 创建数据库连接模块 [database.py](docs/database_py.md)
- 实现异步PostgreSQL连接
- 配置SQLAlchemy会话
- 设置数据库模型基类

2. PostgreSQL设置：
```bash
# 创建数据库
createdb dbname

# 验证连接
psql -d dbname -U user
```

### 4. Redis配置
1. 创建Redis连接模块 [redis.py](docs/redis_py.md)
- 配置Redis客户端
- 实现依赖注入

2. Redis服务配置：
```bash
# 启动Redis服务
net start Redis  # Windows
sudo service redis start  # Linux

# 设置密码
redis-cli
config set requirepass atomic

# 测试连接
redis-cli
auth atomic
ping  # 应返回 PONG
```

### 5. 用户模型开发
1. 创建数据库模型 [models/user.py](docs/models_user_py.md)
- 定义用户表结构
- 配置字段属性
- 设置时间戳

2. 创建数据验证模式 [schemas/user.py](docs/schemas_user_py.md)
- 实现请求验证
- 定义响应格式
- 配置数据转换

### 6. 数据库迁移
详细说明请参考 [数据库迁移文档](docs/migrations.md)

1. 初始化迁移：
```bash
# 创建迁移环境
alembic init migrations

# 创建用户表迁移
alembic revision -m "create users table"
```

2. 应用迁移：
```bash
# 升级到最新版本
alembic upgrade head

# 验证迁移状态
alembic current
```

### 7. API开发
详细说明请参考：
- [用户API文档](memobase_server/api/api_users.md)
- [API测试文档](memobase_server/api/api_testing.md)

1. 创建用户API接口：
- 用户注册
- 获取用户信息
- 获取用户列表

2. 启动服务器：
```bash
uvicorn memobase_server.main:app --reload --port 8080
```

3. 访问API文档：
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

4. 测试API：
```powershell
# Windows PowerShell
Invoke-RestMethod -Method Post -Uri "http://localhost:8080/api/v1/users/" `
                 -ContentType "application/json" `
                 -Body '{"email":"test@example.com","full_name":"测试用户","password":"password123"}'
```

## 验证步骤

### 数据库验证
```python
# 在Python交互式环境中测试
from memobase_server.database import AsyncSessionLocal
from memobase_server.models.user import User

async def test_db():
    async with AsyncSessionLocal() as session:
        try:
            result = await session.query(User).first()
            print("数据库连接成功")
        except Exception as e:
            print(f"数据库连接失败: {e}")
```

### Redis验证
```python
# 在Python交互式环境中测试
from memobase_server.redis import redis_client

try:
    redis_client.ping()
    print("Redis连接成功")
except Exception as e:
    print(f"Redis连接失败: {e}")
```

### API验证
```bash
# 创建用户
curl -X POST "http://localhost:8080/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","full_name":"测试用户","password":"password123"}'

# 获取用户列表
curl "http://localhost:8080/api/v1/users/"
```

## 项目文档

详细文档请参考：

### 系统配置
- [配置系统说明](docs/config_py.md)
- [数据库配置说明](docs/database_py.md)
- [Redis配置说明](docs/redis_py.md)

### 数据模型
- [用户模型说明](docs/models_user_py.md)
- [数据验证说明](docs/schemas_user_py.md)

### 数据库迁移
- [数据库迁移说明](docs/migrations.md)

### API文档
- [用户API接口说明](memobase_server/api/api_users.md)
- [API测试说明](memobase_server/api/api_testing.md)

## 待办事项
- [x] 实现基础项目结构
- [x] 配置数据库连接
- [x] 设置Redis缓存
- [x] 创建用户模型
- [x] 添加数据库迁移
- [x] 实现用户API
- [ ] 实现用户认证
- [ ] 实现备忘录CRUD
- [ ] 添加单元测试
- [ ] 配置CI/CD