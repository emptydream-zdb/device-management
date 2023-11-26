## 日志接口API：json格式
### 设备鉴权/auth
```json
{
    "id": "",
    "password": ""
}
```
### websocket连接建立/echo
由设备发起
ws://xxx.x.x.x:8003/echo?id=...&token=...

### 心跳
```json
{
    "type": "heartbreak",
    "data": {...}
}
```
