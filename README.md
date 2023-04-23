# Python_Devops
the homework code in my Python_Devops class

### requirment：

- sanic
- requests

### 启动命令：
```shell
python3 http_server.py <server_port> <db.csv>
python3 http_client.py <server_ip> <server_port> <input.json> <output.json>
```

实例：
```shell
1 python3 http_server. py 8000 db.csv
2 python3 http_client.py 10.0.0.1 8000 add.json output.json
```

test.json 是测试的输出文件，目前默认server 的启动端口是 0.0.0.0 本地端口
