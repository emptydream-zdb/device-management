import js_csv_convert as cv
import json as js
import requests
import sys

class js_data(object):
    def __init__(self, json_file):
        with open(json_file,"r") as fin:
            json_dict = js.load(fin)
        self.method = json_dict["method"]
        self.data = js.dumps(json_dict["data"])
        self._rq: requests.request
    def run(self, url):
        if self.method == "ADD":
            r = requests.post(url+"/device/add", data = self.data, timeout=0.001)
        elif self.method == "DELETE":
            r = requests.post(url+"/device/del", data = self.data, timeout=0.001)
        elif self.method == "QUERY":
            r = requests.post(url+"/device/get", data = self.data, timeout=0.001)
        elif self.method == "QUERYALL":
            r = requests.get(url+"/device/getall", timeout=0.001)
        self._rq = r
    def get_response(self):
        return self._rq.json()
    def get_status(self):
        return self._rq.status_code
    

class http_client(object):
    
    def __init__(self, client_name: str,url_str:str):
        self.name = client_name
        self.request:js_data = None
        self.url = url_str

    def send(self,json_file):
        self.request = js_data(json_file)
        self.request.run(self.url)
    
    def get_re_json(self):
        return self.request.get_response()
    
    def get_re_code(self):
        return self.request.get_status()


if __name__ == "__main__":
    try:
        server_ip = sys.argv[1]
        server_port = sys.argv[2]
        input_file = sys.argv[3]
        output_file = sys.argv[4]
    except Exception as e:
        print(f"input error: {e}")
    url = "http://"+server_ip+":"+server_port
    http_connect = http_client(input_file,url_str=url)
    http_connect.send(input_file)
    if http_connect.get_re_code() != 200:
        output = {"status": "fail", "data": None}
    else:
        output = http_connect.get_re_json()
    with open(output_file,"w") as fout:
        js.dump(output,fout)
