# 快速启动指南

## 1. 环境准备

### Python环境
```bash
# 确保Python 3.8+已安装
python --version  # 应显示 Python 3.8 或更高版本

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows PowerShell:
# 如果遇到执行策略限制，先执行：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 然后激活虚拟环境：
.\venv\Scripts\Activate.ps1

# Windows CMD:
.\venv\Scripts\activate.bat

# Linux/Mac:
source venv/bin/activate

# 安装依赖
# 方法1：使用requirements.txt（推荐）
pip install -r requirements.txt

# 方法2：单独安装依赖
pip install fastapi>=0.109.0 sqlalchemy>=2.0.25 alembic>=1.13.1 \
    psycopg2-binary>=2.9.9 redis>=5.0.1 pydantic[email]>=2.5.3 \
    python-dotenv>=1.0.0 passlib[bcrypt]>=1.7.4 uvicorn>=0.27.0 \
    python-multipart>=0.0.6 python-jose[cryptography]>=3.3.0 asyncpg>=0.29.0
```

### PowerShell执行策略说明
如果在PowerShell中遇到以下错误：
```
.\venv\Scripts\Activate.ps1 : 无法加载文件 \venv\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。
```

有两种解决方案：

1. 仅为当前用户修改执行策略（推荐）：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. 临时绕过执行策略：
```powershell
PowerShell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
```

选择其中一种方法后，就可以正常激活虚拟环境了。

### PostgreSQL设置
```bash
# 安装PostgreSQL（如果尚未安装）
# Windows: 从 https://www.postgresql.org/download/windows/ 下载安装包

# 创建数据库
createdb memodb

# 创建用户和设置密码（如果需要）
createuser atomic -P
# 按提示输入密码：atomic

# 验证数据库
psql -d memodb -U atomic
# 输入密码后应该能看到 psql 命令提示符
```

### Redis设置
```bash
# Windows安装Redis（如果尚未安装）
# 1. 从 https://github.com/microsoftarchive/redis/releases 下载最新版本
# 2. 运行安装程序
# 3. 将Redis添加到系统环境变量（安装程序通常会自动完成）

# 启动Redis服务
net start Redis

# 设置Redis密码
redis-cli
config set requirepass atomic
exit

# 测试连接
redis-cli
auth atomic
ping  # 应返回 PONG
exit
```

## 2. 项目配置

### 创建配置文件
在项目根目录创建 `.env` 文件：
```env
# 数据库配置
DATABASE_URL=postgresql://atomic:atomic@localhost:5432/memodb

# Redis配置
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=atomic

# API配置
API_VERSION=v1
SECRET_KEY=your-secret-key-here  # 建议使用随机生成的密钥
DEBUG=True  # 生产环境设置为False
```

## 3. 数据库迁移

```bash
# 应用数据库迁移
alembic upgrade head

# 验证迁移状态
alembic current
```

## 4. 启动服务器

```bash
# 开发模式启动
uvicorn memobase_server.main:app --reload --port 8080
```

## 5. 验证安装

### 1. 检查API文档
访问以下地址：
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

### 2. 测试健康检查
```bash
# 使用curl（如果已安装）
curl http://localhost:8080/health

# 或使用PowerShell
Invoke-RestMethod -Uri "http://localhost:8080/health"
# 两种方法都应返回: {"status": "healthy"}
```

### 3. 测试用户API
```powershell
# 创建用户
Invoke-RestMethod -Method Post -Uri "http://localhost:8080/api/v1/users/" -ContentType "application/json" -Body '{"email":"test@example.com","full_name":"测试用户","password":"password123"}'

# 获取用户列表
Invoke-RestMethod -Method Get -Uri "http://localhost:8080/api/v1/users/"
```

## 常见问题

### Python相关问题
1. 确保Python版本 >= 3.8
2. 虚拟环境激活失败时检查执行策略
3. 依赖安装失败时尝试更新pip：
   ```bash
   python -m pip install --upgrade pip
   ```

### 数据库连接错误
1. 检查PostgreSQL服务是否运行
2. 验证数据库用户名和密码
3. 确认数据库 `memodb` 已创建
4. 检查防火墙是否允许本地连接

### Redis连接错误
1. 确认Redis服务正在运行：
   ```bash
   sc query Redis
   ```
2. 验证Redis密码是否正确设置
3. 检查Redis端口是否正确（默认6379）
4. 检查防火墙设置

### API启动问题
1. 确保所有依赖都已安装
2. 检查端口8080是否被占用：
   ```powershell
   netstat -ano | findstr :8080
   ```
3. 查看uvicorn启动日志是否有错误信息

## 下一步

1. 查看详细文档：
   - [配置说明](config_py.md)
   - [数据库配置](database_py.md)
   - [Redis配置](redis_py.md)

2. 开始开发：
   - [用户API文档](../memobase_server/api/api_users.md)
   - [API测试指南](../memobase_server/api/api_testing.md) 