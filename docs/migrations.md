# 数据库迁移说明

## 简单解释

数据库迁移就像是数据库的"版本控制"：
- 记录数据库结构的每次变更
- 可以前进（升级）或后退（回滚）数据库版本
- 确保团队中所有人的数据库结构保持一致

## 迁移文件结构

### 配置文件
- `alembic.ini`: 主配置文件
  * 设置数据库连接
  * 配置迁移脚本位置
  * 其他alembic设置

### 迁移环境
- `migrations/env.py`: 迁移环境配置
  * 连接数据库模型
  * 设置迁移上下文
  * 处理在线和离线迁移

### 版本文件
- `migrations/versions/`: 存放所有迁移版本
  * 每个文件代表一次数据库变更
  * 包含升级和降级操作
  * 自动生成的唯一标识符

## 基本操作

### 创建新迁移
```bash
# 创建新的迁移版本
alembic revision -m "描述变更内容"

# 自动生成迁移（基于模型变化）
alembic revision --autogenerate -m "描述变更内容"
```

### 执行迁移
```bash
# 升级到最新版本
alembic upgrade head

# 升级指定版本
alembic upgrade <revision_id>

# 回滚到上一个版本
alembic downgrade -1

# 回滚到基础版本
alembic downgrade base
```

### 查看状态
```bash
# 查看当前版本
alembic current

# 查看历史记录
alembic history
```

## 当前迁移版本

### 用户表迁移 (89ee7b00c3d2)
创建基础用户表，包含以下字段：
- `id`: 用户ID（主键）
- `email`: 电子邮箱（唯一索引）
- `full_name`: 用户全名
- `hashed_password`: 加密密码
- `created_at`: 创建时间
- `updated_at`: 更新时间

## 最佳实践

1. 迁移文件命名
   - 使用清晰的描述性名称
   - 包含操作类型（create/update/delete）
   - 指明影响的表名

2. 版本控制
   - 迁移文件要提交到版本控制系统
   - 不要修改已提交的迁移文件
   - 如需修改，创建新的迁移版本

3. 测试
   - 在应用迁移前先在测试环境验证
   - 确保 upgrade 和 downgrade 都能正常工作
   - 检查数据完整性 