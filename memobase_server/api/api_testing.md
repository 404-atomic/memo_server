# API测试文档

## PowerShell测试示例

### 创建用户

使用PowerShell的`Invoke-RestMethod`命令测试API：

```powershell
Invoke-RestMethod -Method Post -Uri "http://localhost:8080/api/v1/users/" `
                 -ContentType "application/json" `
                 -Body '{"email":"test@example.com","full_name":"测试用户","password":"password123"}'
```

#### 请求说明
- 方法：`POST`
- 端点：`/api/v1/users/`
- 内容类型：`application/json`
- 请求体：
  ```json
  {
      "email": "test@example.com",
      "full_name": "测试用户",
      "password": "password123"
  }
  ```

#### 响应结果
```
email      : test@example.com
full_name  : 测试用户
id         : 1
created_at : 2025-02-10T08:31:27.254779Z
updated_at :
```

#### 注意事项
1. 中文编码处理
   - PowerShell可能会显示中文字符为`????`
   - 这是PowerShell的显示问题，实际数据库中存储的是正确的中文
   - 可以通过API获取验证中文是否正确存储

2. 时间格式
   - 返回的时间格式为ISO 8601
   - 包含时区信息（Z表示UTC时间）
   - `updated_at`为空是正常的（新创建的用户）

### 其他测试命令

#### 获取单个用户
```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:8080/api/v1/users/1"
```

#### 获取用户列表
```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:8080/api/v1/users/?skip=0&limit=10"
```

## 使用curl测试（Windows PowerShell）

### 创建用户
```powershell
curl.exe -X POST "http://localhost:8080/api/v1/users/" `
         -H "Content-Type: application/json" `
         -d "{\"email\":\"test@example.com\",\"full_name\":\"测试用户\",\"password\":\"password123\"}"
```

### 获取用户
```powershell
curl.exe "http://localhost:8080/api/v1/users/1"
```

### 获取用户列表
```powershell
curl.exe "http://localhost:8080/api/v1/users/?skip=0&limit=10"
```

## 常见问题解决

### 中文显示问题
1. 使用`-Encoding UTF8`参数：
```powershell
$Body = @{
    email = "test@example.com"
    full_name = "测试用户"
    password = "password123"
} | ConvertTo-Json

Invoke-RestMethod -Method Post `
                 -Uri "http://localhost:8080/api/v1/users/" `
                 -ContentType "application/json" `
                 -Body $Body `
                 -Encoding UTF8
```

### 验证数据正确性
1. 使用浏览器访问Swagger文档：
   - 打开 http://localhost:8080/docs
   - 使用Swagger UI测试API
   - 可以正确显示中文

2. 使用数据库工具直接查询：
```sql
SELECT * FROM users WHERE id = 1;
```

## 测试检查清单
- [ ] 创建用户成功
- [ ] 邮箱格式验证正常
- [ ] 中文存储正确
- [ ] ID自动递增
- [ ] 时间戳正确生成
- [ ] 密码正确加密
- [ ] 响应格式符合预期 