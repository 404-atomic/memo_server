# 用户API接口说明

## 接口概述

用户管理API提供以下功能：
- 创建新用户
- 获取单个用户信息
- 获取用户列表

所有接口都位于 `/api/v1/users` 路径下。

## API端点

### 创建用户

```http
POST /api/v1/users/
```

请求体：
```json
{
    "email": "user@example.com",
    "full_name": "测试用户",
    "password": "secure_password"
}
```

响应示例：
```json
{
    "id": 1,
    "email": "user@example.com",
    "full_name": "测试用户",
    "created_at": "2024-02-10T10:00:00",
    "updated_at": null
}
```

### 获取单个用户

```http
GET /api/v1/users/{user_id}
```

参数：
- `user_id`: 用户ID（路径参数）

响应示例：
```json
{
    "id": 1,
    "email": "user@example.com",
    "full_name": "测试用户",
    "created_at": "2024-02-10T10:00:00",
    "updated_at": null
}
```

### 获取用户列表

```http
GET /api/v1/users/
```

查询参数：
- `skip`: 跳过的记录数（默认：0）
- `limit`: 返回的最大记录数（默认：100）

响应示例：
```json
[
    {
        "id": 1,
        "email": "user1@example.com",
        "full_name": "用户1",
        "created_at": "2024-02-10T10:00:00",
        "updated_at": null
    },
    {
        "id": 2,
        "email": "user2@example.com",
        "full_name": "用户2",
        "created_at": "2024-02-10T11:00:00",
        "updated_at": null
    }
]
```

## 错误处理

### 404 Not Found
当请求的用户不存在时：
```json
{
    "detail": "User not found"
}
```

### 422 Validation Error
当请求数据格式不正确时：
```json
{
    "detail": [
        {
            "loc": ["body", "email"],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```

## 安全说明

- 密码在存储前会进行加密处理
- 返回的用户信息中不包含密码
- 邮箱地址要求唯一

## 使用示例

### 使用curl创建用户
```bash
curl -X POST "http://localhost:8080/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","full_name":"测试用户","password":"password123"}'
```

### 使用curl获取用户
```bash
curl "http://localhost:8080/api/v1/users/1"
```

### 使用curl获取用户列表
```bash
curl "http://localhost:8080/api/v1/users/?skip=0&limit=10"
``` 