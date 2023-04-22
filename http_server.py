import sys,os
import json as js
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic import response as rp
import js_csv_convert as cv

try:
    server_port = int(sys.argv[1])
    db_file = sys.argv[2]
    db_path = os.path.join(".",db_file)
except Exception as e:
    print(f"input error: {e}")

app = Sanic("http_server")

async def find_device(id_list: list, db_list: list) -> list:
    """ return the finded device index in db_list
    :parm: id_list: list   the list of the device or the id to find
           db_list: list   the list of the device in db 
    """
    res_list = []
    for device in id_list:
        if type(device) == dict: # judge element in id_list is id or device
            dev_id = device["id"]
        else:
            dev_id = device
        for x in range(len(db_list)):
            if str(db_list[x]["id"]) == str(dev_id): # find the index and insert the res_list
                res_list.append(x)
                break
    return res_list

@app.get("/device/getall", name="/device/getall")
async def get_all_device(request):
    """solve the getall request
       method: get
       response: json  The all device data
    """
    response = {"status": "success","data": cv.csv_to_js(db_path)}
    return rp.json(response)


@app.post("/device/add", name="device/add")
async def add_device(request):
    """solve the add request
       method: post
       response: json  The status of the resul: sucess or fail
    """
    re_info = request.json
    dataList = cv.csv_to_js(db_path) # read db_data as a list
    finded_index = await find_device(re_info, dataList) 
    if len(finded_index) == 0: # the device to add is not in db 
        cv.js_to_csv(re_info,"db.csv",mode='a')
        result = {"status": "success", "data": None}
    else: # the device to add is in db 
        result = {"status": "fail", "data": None}
    return rp.json(result)


@app.post("/device/del", name="device/del")
async def del_device(request):
    """solve the del request
       method: post
       response: json  The status of the resul: sucess or fail
    """
    re_info = request.json
    dataList = cv.csv_to_js(db_path)# read db_data as a list
    finded_index = await find_device(re_info, dataList)
    if len(finded_index) != 0: # delate the device
        for x in reversed(finded_index):
            dataList.pop(x)
        cv.js_to_csv(dataList,"db.csv",mode='w')
        result = {"status": "success", "data": None}
    else: # db does not have the device to del
        result = {"status": "fail", "data": None}
    return rp.json(result)


@app.post("/device/get", name="device/get")
async def get_device(request):
    """solve the get request
       method: post
       response: json  The status of the resul: sucess or fail ,and the device data which to get
    """
    re_info = request.json
    dataList = cv.csv_to_js(db_path)# read db_data as a list
    finded_index = await find_device(re_info, dataList)
    if len(finded_index) != 0:
        result = {"status": "success", "data":[dataList[x] for x in finded_index]}
    else: # db does not have the device to get
        result = {"status": "fail", "data": None}
    return rp.json(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=server_port) 