from sanic import Sanic
from sanic.request import Request
from sanic.response import json,text
import DBcontrol
import sys,time
app = Sanic("DBserver")

host = "localhost"
user = "root"
passwd = "251314"
database = "Dev"

DB = DBcontrol.deviceDB(host,user,passwd,database)

@app.post("/add",name="add")
async def add(request):
    req_data = request.json
    if req_data["method"] == "add_device":
        message = DB.add_device(req_data["data"])
    elif req_data["method"] == "add_group":
        message = DB.add_group(req_data["data"])
    elif req_data["method"] == "add_relation":
        message = DB.add_relation(req_data["data"])
    else:
        return json({"version": "1.0","result": False,"message":"method not exist!","data": None})
    if DB.flag:
        return json({"version": "1.0","result": True,"message":"success!","data":None})
    return json({"version": "1.0","result": False,"message":message,"data":None})

@app.put("/update",name="update")
async def update(request):
    req_data = request.json
    if req_data["method"] == "update_device":
        message = DB.update_device(req_data["data"])
    elif req_data["method"] == "update_group":
        message = DB.update_group(req_data["data"])
    elif req_data["method"] == "update_relation":
        message = DB.update_relation(req_data["data"])
    else:
        return json({"version": "1.0","result": False,"message":"method not exist!","data":None})
    if DB.flag:
        return json({"version": "1.0","result": True,"message":"success!","data":None})
    return json({"version": "1.0","result": False,"message":message,"data":None})

@app.post("/query",name="query")
async def query(request):
    req_data = request.json
    if req_data["method"] == "get_all_device":
        res = DB.get_all_device()
    elif req_data["method"] == "get_all_device_and_group":
        res = DB.get_all_device_and_group()
    elif req_data["method"] == "get_all_group":
        res = DB.get_all_group()
    elif req_data["method"] == "get_device_by_id":
        res = DB.get_device_by_id(req_data["data"])
    elif req_data["method"] == "get_device_by_group":
        res = DB.get_device_by_group(req_data["data"])
    elif req_data["method"] == "get_device_and_group_by_id":
        res = DB.get_device_and_group_by_id(req_data["data"])
    elif req_data["method"] == "get_group_by_num":
        res = DB.get_group(req_data["data"])        
    else:
        return json({"version": "1.0","result": False,"message":"method not exist!","data":None})
    if DB.flag:
        return json({"version": "1.0","result": True,"message":"success!","data":res})
    return json({"version": "1.0","result": False,"message":"","data":None})

@app.post("/delete",name="delete")
async def delete(request):
    req_data = request.json
    if req_data["method"] == "delete_group":
        message = DB.del_group(req_data["data"])
    elif req_data["method"] == "delete_device":
        message = DB.del_device(req_data["data"])
    elif req_data["method"] == "delete_relation":
        message = DB.del_relation(req_data["data"])
    else:
        return json({"version": "1.0","result": False,"message":"method not exist!","data":None})
    if DB.flag:
        return json({"version": "1.0","result": True})
    return json({"version": "1.0","result": False,"message":message,"data":None})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
