# models/user.py 用户模型说明

## 代码详解

### 导入部分

主要导入以下组件：
- `Column`: SQLAlchemy的列定义
- `Integer, String, DateTime`: 数据类型
- `func`: SQL函数（用于时间戳）
- `Base`: 在database.py中创建的基类

### User类定义
```python
class User(Base):
    __tablename__ = "users"
```
- 继承自`Base`类
- 通过`__tablename__`定义表名为"users"

### 字段说明

#### 基本字段
- `id`: 自增主键，整数类型
  ```python
  id = Column(Integer, primary_key=True, index=True)
  ```

- `email`: 用户邮箱，字符串类型，唯一索引
  ```python
  email = Column(String, unique=True, index=True)
  ```

- `full_name`: 用户全名，字符串类型
  ```python
  full_name = Column(String)
  ```

- `hashed_password`: 加密后的密码，字符串类型
  ```python
  hashed_password = Column(String)
  ```

#### 时间戳字段
- `created_at`: 创建时间
  ```python
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  ```
  - 自动设置为记录创建时的时间
  - 包含时区信息

- `updated_at`: 更新时间
  ```python
  updated_at = Column(DateTime(timezone=True), onupdate=func.now())
  ```
  - 在记录更新时自动更新
  - 包含时区信息

## 使用说明

该模型用于：
- 定义用户表的数据库结构
- 提供ORM接口进行数据库操作
- 确保数据完整性和一致性 