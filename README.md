# cxsj-crud-backend

🎉创新实践1️⃣期末项目后端，一个具备基本增删差改功能的后端。

访问地址：https://cxsj.kinoko.fun

## 基于docker使用项目

默认运行在本地的8020端口。

```bash
docker build -t cxsj2412:v0.0 .
```
```bash
docker run -d -p 8020:8020 --name my-flask-app cxsj2412:v0.0
```

## API接口列表

- GET /ping
- GET /students
- POST /students
- PUT /students/\<id\>
- DELETE /students/\<id\>

### GET /ping 测试服务是否可访问

请求

```http
GET /ping HTTP/1.1
Host: localhost:8020
```

响应

```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```

### GET /students 获取所有学生信息

请求

```http
GET /students HTTP/1.1
Host: localhost:8020
```

响应（假设数据库中有5个学生）

```json
{
    "code": 200,
    "message": "success",
    "data": [
        {"id": 1, "name": "Alice", "age": 20, "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "age": 22, "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "age": 23, "email": "charlie@example.com"},
        {"id": 4, "name": "David", "age": 21, "email": "david@example.com"},
        {"id": 5, "name": "Eve", "age": 24, "email": "eve@example.com"}
    ]
}
```


### POST /students 增加单个学生信息

请求

```http
POST /students HTTP/1.1
Host: localhost:8020
Content-Type: application/json

{
    "name": "John",
    "age": 25,
    "email": "john@example.com"
}
```

响应

```json
{
    "code": 200,
    "message": "success",
    "data": {"id": 6, "name": "John", "age": 25, "email": "john@example.com"}
}
```

错误示例（缺少字段）

```http
POST /students HTTP/1.1
Host: localhost:8020
Content-Type: application/json

{
    "name": "John"
}
```

兜底响应

```json
{
    "code": 400,
    "message": "Invalid input",
    "data": {}
}
```

### PUT /students/\<id\> 根据ID更新单个学生信息

请求

```http
PUT /students/1 HTTP/1.1
Host: localhost:8020
Content-Type: application/json

{
    "name": "John Doe",
    "age": 26,
    "email": "john.doe@example.com"
}
```

响应

```json
{
    "code": 200,
    "message": "success",
    "data": {"id": 1, "name": "John Doe", "age": 26, "email": "john.doe@example.com"}
}
```

错误示例（ID为字母）

```http
PUT /students/abc HTTP/1.1
Host: localhost:8020
Content-Type: application/json

{
    "name": "John Doe",
    "age": 26,
    "email": "john.doe@example.com"
}
```

兜底响应

```json
{
    "code": 400,
    "message": "Invalid ID",
    "data": {}
}
```

### DELETE /students/\<id\> 根据ID删除单个学生

请求

```http
DELETE /students/1 HTTP/1.1
Host: localhost:8020
```

响应

```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```

错误示例（ID为字母）

```http
DELETE /students/abc HTTP/1.1
Host: localhost:8020
```

兜底响应

```json
{
    "code": 400,
    "message": "Invalid ID",
    "data": {}
}
```

### GET /students/\<id\> 根据ID获取单个学生信息

请求

```http
GET /students/1 HTTP/1.1
Host: localhost:8020
```

响应

```json
{
    "code": 200,
    "data": {
        "age": 20,
        "email": "alice@example.com",
        "id": 1,
        "name": "Alice"
    },
    "message": "success"
}
```

错误请求（ID为字母）

```http
GET /students/a HTTP/1.1
Host: localhost:8020
```

兜底响应

```json
{
    "code": 400,
    "data": {},
    "message": "Invalid ID"
}
```