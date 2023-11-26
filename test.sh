curl -X POST 'http://127.0.0.1:8000/register' -d '{"version": "1.0","method": "add_device","data":[{"id":"62292971188077901342","name": "west1","type": "doll",
        "state": "up","hardware": {"sn": "000001","model": "000002"},"software": {"base": {"version": "1.0","lastUpdate": "2023-6-15",
        "status": "up"},"work": {"version": "2.0","lastUpdate": "2023-6-15","status": "up"}},"nic": {"eth": {"mac": "ad:83:ff:14",
        "ipv4": "8.12.54.8"},"wifi": {"mac": "11:11:11:11","ipv4": "1.1.1.1"}},"LTE_IMEI": "test1"}]}' 

# {"version":"1.0","result":true,"message":"success!","data":[{"id":"81846894092237472031","passwd":"qJI8Q4P2WJQSHBStAVaf"}]}


curl -X POST 'http://127.0.0.1:8000/register' -d '{"version": "1.0","method": "register_device","data":[{"name": "west2","type": "doll",
        "state": "up","hardware": {"sn": "100001","model": "100002"},"software": {"base": {"version": "1.0","lastUpdate": "2023-6-15",
        "status": "up"},"work": {"version": "2.0","lastUpdate": "2023-6-15","status": "up"}},"nic": {"eth": {"mac": "22:22:22:22",
        "ipv4": "2.2.2.2"},"wifi": {"mac": "33:33:33:33","ipv4": "4.4.4.4"}},"LTE_IMEI": "test2"}]}'
# {"version":"1.0","result":true,"message":"success!","data":[{"id":"03704790943691253431","passwd":"Fz5xPVamuV_8-eRN8MhB"}]}%
    
curl -X POST 'http://127.0.0.1:8000/add' -d '{
    "version": "1.0",
    "method": "add_group",
    "data": [{ 
        "group_num": "2",
        "group_name": "qingshuihe",
        "description": "qingshuihe 的大门"
    }]
}'
# {"version":"1.0","result":true,"message":"success!","data":null}%

curl -X POST 'http://127.0.0.1:8000/add' -d '{
    "version": "1.0",
    "method": "add_relation",
    "data":[{
        "id": "55215655658334517346",
        "group_num": "1"
    }]
}'
# {"version":"1.0","result":true,"message":"success!","data":null}%

curl -X POST 'http://127.0.0.1:8000/get' -d '
{
    "version": "1.0",
    "method": "get_all_device",
    "data": []
}'

# 日志查询
curl http://127.0.0.1:8001/query -d '{
    "logtype": "database",
    "begintime": null
}'

# 设备登陆
curl http://127.0.0.1:8003/auth -d '{
    "id": "81846894092237472031",
    "password": "qJI8Q4P2WJQSHBStAVaf"
}'