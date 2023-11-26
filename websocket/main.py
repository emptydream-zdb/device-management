from sanic import Sanic, response
from sys import argv
import json
import requests

import verify

app = Sanic("WebSocketApp")


def getJsonData(json_file: str) -> list:
    """使用json代替数据库进行读取，用于调试"""
    f = open(json_file)
    data = json.load(f)
    f.close()

    if type(data) is dict:
        temp: list = []
        temp.append(data)
        data = temp
    return data

def uploadLogging(j: dict):
    requests.post("http://127.0.0.1:8001/upload",json=j)

def getDBData(id: str) -> list:
    templist: list = []
    templist.append(id)

    resp = requests.post("http://127.0.0.1:8002/query",
        json={
            "method": "get_device_by_id",
            "datatype": "id",
            "data": templist
        })
    if resp.json()["result"]:
        data = resp.json()["data"][0]
    else:
        data = None
    return data


@app.middleware("response")
async def add_csp(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Request-Headers"] = "*"

@app.post("/auth")
async def auth(request):
    """
    /auth 设备登录鉴权：
        根据接收的用户密码值，用密码加上数据库内的salt进行哈希散列，
        生成的值与数据库内密文进行比对，相同则鉴权成功，反之则反
    """

    recv = request.json

    uploadLogging({
                "logtype": "deviceLogin",
                "data": {
                    "id": recv["id"],
                    "msg": "device send link request"
                }
            })

    data = getDBData(recv["id"])

    resp = verify.pwdComp(data, recv)
    if data != None and resp["status"] == 0:
        resp["token"] = verify.generateToken(recv["id"])
        uploadLogging({
            "logtype": "deviceLogin",
            "data": {
                "id": recv["id"],
                "status": 0,
                "msg": "Authentication success"
            }
        })
    else:
        uploadLogging({
            "logtype": "deviceLogin",
            "data": {
                "id": id,
                "status": -1,
                "msg": "Authentication failed"
            }
        })
    return response.json(resp)


@app.on_request
async def auth_ws_token(request):
    if request.json == None:
        args = request.args
        if "id" in args and "token" in args:
            id = args["id"][0]
            token = args["token"][0]

            if verify.verifyToken(id, token) == False:
                uploadLogging({
                    "logtype": "deviceLogin",
                    "data": {
                        "id": id,
                        "status": 0,
                        "msg": "websocket link failed"
                    }
                })
                return response.empty(status=401)
            uploadLogging({
                "logtype": "deviceLogin",
                "data": {
                    "id": id,
                    "status": 0,
                    "msg": "websocket link success"
                }
            })
    return None


@app.websocket("/echo")
async def echo(request, ws):
    while True:
        data = await ws.recv()
        data = json.loads(data)
        if data["type"] == "heartbreak":
            uploadLogging({
                "logtype": "heartbreak",
                "data": data["data"]
            })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
