import os,time
import requests,websockets

front_server = "http://127.0.0.1:8000"
sock_url = "http://127.0.0.1:8003"

print("添加device")
req = {"version": "1.0","method": "register_device","data":[{"name": "west1","type": "doll",
        "state": "up","hardware": {"sn": "000001","model": "000002"},"software": {"base": {"version": "1.0","lastUpdate": "2023-6-15",
        "status": "up"},"work": {"version": "2.0","lastUpdate": "2023-6-15","status": "up"}},"nic": {"eth": {"mac": "ad:83:ff:14",
        "ipv4": "8.12.54.8"},"wifi": {"mac": "11:11:11:11","ipv4": "1.1.1.1"}},"LTE_IMEI": "test1"}]}
print(req)
res = requests.post(front_server + "/register", json = req)
dev_id = res.json()["data"][0]["id"]
passwd = res.json()["data"][0]["passwd"]
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")

print("添加group")
req = {
    "version": "1.0",
    "method": "add_group",
    "data": [{ 
        "group_num": "1",
        "group_name": "清水河",
        "description": "清水河的大门"
    }]
}
print(req)
res = requests.post(front_server + "/add", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")

print("添加relation")
req = {
    "version": "1.0",
    "method": "add_relation",
    "data": [{
        "id": dev_id,
        "group_num": "1"
    }]
}
print(req)
res = requests.post(front_server + "/add", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("查询all_device")
req = {
    "version": "1.0",
    "method": "get_all_device",
    "data": []
}
print(req)
res = requests.post(front_server + "/get", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("查询device_by_id")
req = {
    "version": "1.0",
    "method": "get_device_by_id",
    "data": [dev_id]
}
print(req)
res = requests.post(front_server + "/get", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("查询get_all_device_and_group")
req = {
    "version": "1.0",
    "method": "get_all_device_and_group",
    "data": []
}
print(req)
res = requests.post(front_server + "/get", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("查询get_all_group")
req = {
    "version": "1.0",
    "method": "get_all_group",
    "data": []
}
print(req)
res = requests.post(front_server + "/get", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("更新device")
req = {"version": "1.0","method": "update_device","data":[{"id":dev_id,"name": "west1","type": "car",
        "state": "up","hardware": {"sn": "000001","model": "000002"},"software": {"base": {"version": "1.0","lastUpdate": "2023-6-15",
        "status": "up"},"work": {"version": "2.0","lastUpdate": "2023-6-15","status": "up"}},"nic": {"eth": {"mac": "ad:83:ff:14",
        "ipv4": "8.12.54.8"},"wifi": {"mac": "11:11:11:11","ipv4": "1.1.1.1"}},"LTE_IMEI": "test2"}]}
print(req)
res = requests.post(front_server + "/update", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("更新group")
req = {
    "version": "1.0",
    "method": "update_group",
    "data": [{ 
        "group_num": "1",
        "group_name": "沙河",
        "description": "沙河的大门"
    }]
}
print(req)
res = requests.post(front_server + "/update", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("删除device")
req = {
    "version": "1.0",
    "method": "delete_device",
    "data": [dev_id]
}
print(req)
res = requests.post(front_server + "/delete", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")


print("删除group")
req = {
    "version": "1.0",
    "method": "delete_group",
    "data": ["1"]
}
print(req)
res = requests.post(front_server + "/delete", json = req)
print("响应")
print(res.json())
time.sleep(2)
os.system("clear")