# The API doc in front server

## [POST] /register

- 请求body:

```json
{
    "version": "1.0",
    "method": "register_device",
    "data":{
        "name": "",
        "type": "",
        "state": "",
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
}
```

- 响应 body:

```json
{//出错时
    "result": False,
    "message":"",
    "data": null
} 
{//成功时
    "version": "1.0",
    "result": True,
    "message":"success!",
    "data":[
        {
            "id": ,
            "passwd"
        }
    ]/null  //没有时为null
}
```

## [POST] /add

更新设备信息/更新分组信息/更新关系信息

- 请求body

```json
{
    "version": "1.0",
    "method": "add_group"/"add_relation",
    "data": { // 添加分组
        "group_num": "",
        "group_name": "",
        "description": "",
    },
    "data":{
        "id": "",
        "group_num": ""
    }
}
```

- 响应 body:

```json
{//错误时
    "result": False,
    "message":"",
    "data": null
} // 
{//正确时
    "result": True,
    "message":"success!",
    "data": null  //没有时为null
}
```

## [PUT] /update

更新设备信息/更新分组信息/更新关系信息

- 请求body

```json
{
    "version": "1.0",
    "method": "update_device"/"update_group"/"update_erlation",
    "data": {
        "id"/"group_num": "",//更新什么就是什么
        "time":"",
        //其余需要更改的信息
    },
}
```

- 响应 body:

```json
{//错误时
    "result": False,
    "message":"",
    "data": null
} // 
{//正确时
    "result": True,
    "message":"success!",
    "data":null  //没有时为null
}
```

## [POST] /get

- 请求 body
  
```json
{
    "version": "1.0",
    "method": "get_status_log"/"get_login_log"/"get_database_log"/"get_all_device"/"get_all_device_and_group"/"get_all_group"/"get_device_by_id"/"get_device_by_group"/"get_device_and_group_by_id"/"get_group_by_num",
    "data": []
}
```

- 响应 body

```json
{//错误时
    "result": False,
    "message":"",
    "data": null
} // 
{//正确时
    "result": True,
    "message":"success!",
    "data":[
        {},
        {}
    ]/null  //没有时为null
}
```

## [POST] /delete

- 请求 body

```json
{
    "version": "1.0",
    "method":"delete_group"/"delete_device"/"delete_relation",
    "data": []// id 或者 group_num 的list
}
```

- 响应 body

```json
{//错误时
    "result": False,
    "message":"",
    "data": null
} // 
{//正确时
    "result": True,
    "message":"success!",
    "data":null  //没有时为null
}
```
