# 导入FastAPI相关组件
from fastapi import FastAPI
from .core.config import settings
from .api.v1.endpoints import users
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用程序生命周期管理器
    用于处理启动和关闭时的操作
    例如：数据库连接、缓存预热等
    """
    # 启动时的操作
    # 例如：初始化数据库连接池
    yield
    # 关闭时的操作
    # 例如：关闭数据库连接、清理资源

# 创建FastAPI应用实例
app = FastAPI(
    title="Memobase API",  # API文档标题
    version=settings.API_VERSION,  # API版本号
    lifespan=lifespan  # 生命周期管理器
)

# 注册路由
# prefix：URL前缀，例如：/api/v1/users
# tags：用于API文档分组
app.include_router(
    users.router,
    prefix=f"{settings.API_PREFIX}/users",
    tags=["users"]
)

# 健康检查端点
# 用于监控系统检查API服务是否正常运行
@app.get("/health")
async def health_check():
    """
    健康检查端点
    返回：{"status": "healthy"}
    用途：
    1. 负载均衡器健康检查
    2. 容器编排系统就绪探针
    3. 监控系统状态检查
    """
    return {"status": "healthy"} 