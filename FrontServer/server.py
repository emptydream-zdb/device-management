from sanic import Sanic
from sanic.request import Request
from sanic.response import json
import sys,time,string,secrets,hashlib
import requests
import ujson as js

# DB_url = sys.argv[1]
DB_url = "http://127.0.0.1:8002"
log_url = "http://127.0.0.1:8001"

app = Sanic("server")

async def gen_id(length):
    return ''.join([secrets.choice(string.digits) for i in range(length)])
async def gen_salt(length):
    return ''.join([secrets.choice(string.ascii_letters+string.digits) for i in range(length)])


def uploadLogging(j: dict):
    requests.post("http://127.0.0.1:8001/upload", json=j)


@app.middleware("response")
async def add_csp(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Request-Headers"] = "*"

@app.post("/register",name="register")
async def register(request):
    req = request.json
    req_data = req["data"]
    res_data = []
    for x in req_data:
        id = await gen_id(20)
        passwd = secrets.token_urlsafe(15)
        salt = await gen_salt(30)
        secret = hashlib.sha256((id+passwd+salt).encode()).hexdigest()
        x["id"] = id
        x["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        x["auth"] = {"salt":salt,"secret":secret}
        res_data.append({"id":id,"passwd":passwd})
    req["method"] = "add_device"
    db_res = requests.post(DB_url + "/add", json = req)
    res = db_res.json()
    if res["result"]:
        res["data"] = res_data
    uploadLogging({
        "logtype": "database",
        "data": {
            "msg": "register device in database."
        }
    })

    return json(res)

@app.post("/add",name="add")
async def update(request):
    req = request.json
    for x in req["data"]:
        x["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    db_res = requests.post(DB_url + "/add", json = req)
    res = db_res.json()
    uploadLogging({
        "logtype": "database",
        "data": {
            "msg": "add group in database."
        }
    })
    return json(res)

@app.put("/update",name="update")
async def update(request):
    req = request.json
    for x in req["data"]:
        x["time"] = time.strftime("%Y-%m-%d %H:%M:%S")
    db_res = requests.put(DB_url + "/update", json = req)
    res = db_res.json()

    uploadLogging({
        "logtype": "database",
        "data": {
            "msg": "update device in database."
        }
    })

    return json(res) 
    

@app.post("/get",name="get")
async def query(request):
    req = request.json
    if req["method"] == "get_status_log":
        db_res = requests.post(log_url + "/query", json = {"logtype": "heartbreak"})
    elif req["method"] == "get_login_log":
        db_res = requests.post(log_url + "/query", json = {"logtype": "deviceLogin"})
    elif req["method"] == "get_database_log":
        db_res = requests.post(log_url + "/query", json = {"logtype": "database"})
    else:
        db_res = requests.post(DB_url + "/query", json = req)
    res = db_res.json()

    uploadLogging({
        "logtype": "database",
        "data": {
            "msg": "query device from database."
        }
    })

    return json(res)

@app.post("/delete",name="delete")
async def delete(request):
    req = request.json
    db_res = requests.post(DB_url + "/delete", json = req)
    res = db_res.json()

    uploadLogging({
        "logtype": "database",
        "data": {
            "msg": "register device in database."
        }
    })
    
    return json(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)