## 日志接口API：json格式

```json
{
    "logtype": "",
    "begintime": "xxxx-[x]x-[x]x"/null,
    "data": {
        ......
    }
}
```

### 查询日志:/query

```json
{
    "logtype": "deviceLogin"/"heartbreak"/"database"
}
```
返回：
```json
[
    {
        "time": "xxxx-xx-xx",
        "data": [
            "...",
            "...",
            ...
        ]
    },
    ...
]
```

### 上传：北向增删查改

```json
{
    "logtype": "database",
    "data": {
        "msg": ""
    }
}
```

### 上传：设备发起连接、通道建立成功 及 鉴权结果:/upload

设备发起连接：

```json
{
    "logtype": "deviceLogin",
    "data": {
        "id": "..."
        "msg": "device send link request"
    }
}
```

通道建立成功/失败：

```json
{
    "logtype": "deviceLogin".
    "data": {
        "id": "...",
        "status": 0/-1,
        "msg": "websocket link success"/"websocket link failed"
    }
}
```

鉴权结果：

```json
{
    "logtype": "deviceLogin".
    "data": {
        "id": "...",
        "status": 0/-1,
        "msg": "Authentication success"/"Authentication failed"
    }
}
```

### 上传：设备状态信息/upload

```json
{
    "logtype": "hbReport",
    "data": {
        "id": "...",
        "user-cpu-time": "...",
        "system-cpu-time": "...",
        "idle-cpu-time": "...",
        "io-wait-cpu-time": "...",
        ...
    }
}
```
