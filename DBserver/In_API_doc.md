## 内部接口API：json

请求body：

```json
{
    "method":"",
    "data": [] //统一使用list 发送数据，哪怕仅有一个数据, 其中 id:str/ group_num:str/device_info: dict/group_info:dict
}
```

### [POST] /quary

```json
{
    "method": "get_all_device"/"get_all_device_and_group"/"get_all_group"/"get_device_by_id"/"get_device_by_group"/"get_device_and_group_by_id"/"get_group_by_num",
    "data": []
}
```

## [post] /add

```json
{
    "method": "add_device"/"add_group"/"add_relation",
    "data": []
}
```

### [put] /update

```json
{
    "method":"update_device"/"update_group"/"update_erlation",
    "data": []//jian shuo ming
}
```

### [post] /del

```json
{
    "method":"delete_group"/"delete_device"/"delete_relation",
    "data": []//jian shuo ming
}
```

- 调用 增删查 时 data 按照说明发送

- 调用 改 时 data 如下：

#### device_update API 发送的 data 字段

```json
[
    {
        "id": "",
        "time": "",
        //加上需要更新的字段，不更新的不发
    },
    ...
]
```

#### group_update API 发送的 data 字段

```json
[
    {
        "group_num": "",
        "time": "",
        //加上需要更新的字段，不更新的不发
    },
]
```

响应body：

```json
{
    "result": False,
    "message":"",
    "data": null
} // 
{
    "result": True,
    "message":"success!",
    "data":[]/null  //没有时为null
}   //正确
```

### device_info data 字段

```json
{
    "id": "",
    "name": "",
    "type": "",
    "group": "",
    "state": "",
    "auth": {
        "salt": "",
        "secret": ""
    },
    "time": "",
    "hardware": {
        "sn": "",
        "model": ""
    },
    "software": {
        "base": {
            "version": "",
            "lastUpdate": "",
            "status": ""
        },
        "work": {
            "version": "",
            "lastUpdate": "",
            "status": ""
        }
    },
    "nic": {
        "eth": {
            "mac": "",
            "ipv4": ""
        },
        "wifi": {
            "mac": "",
            "ipv4": ""
        }
    },
    "LTE_IMEI": ""
}
```

### group_info data 字段

```json
{
    "group_num": "",
    "group_name": "",
    "description": "",
    "time": ""
}
```

### relation data

```json
{
    "id": "",
    "group_num": ""
}
