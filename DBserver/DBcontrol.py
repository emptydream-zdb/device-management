import pymysql
from pymysql.cursors import DictCursor
from js_csv_convert import _dealDict as dd
from js_csv_convert import _dealunder as du
#TODO 分组表添加内容
#TODO 错误消息相关，错误检测相关

class deviceDB:
    def __init__(self,host:str, user:str,password:str,database:str):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self.db = pymysql.connect(host= host,user= user,passwd= password)
        self.cursor = self.db.cursor(cursor=DictCursor)
        self.flag = True

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.cursor.execute(f"USE {database}")
        sql1 = """CREATE TABLE IF NOT EXISTS device(
            id                          VARCHAR(30) PRIMARY KEY,
            name                        VARCHAR(30),
            type                        VARCHAR(30),
            state                       VARCHAR(10),
            auth_salt                   VARCHAR(30),
            auth_secret                 VARCHAR(64),
            time_register               VARCHAR(30),
            time_update                 VARCHAR(30),
            hardware_sn                 VARCHAR(30),
            hardware_model              VARCHAR(30),
            software_base_version       VARCHAR(30),
            software_base_lastUpdate    VARCHAR(30),
            software_base_status        VARCHAR(30),
            software_work_version       VARCHAR(30),
            software_work_lastUpdate    VARCHAR(30),
            software_work_status        VARCHAR(30),
            nic_eth_mac                 VARCHAR(30),
            nic_eth_ipv4                VARCHAR(30),
            nic_wifi_mac                VARCHAR(30),
            nic_wifi_ipv4               VARCHAR(30),
            LTE_IMEI                    VARCHAR(30)
        )
        """

        sql2 = """CREATE TABLE IF NOT EXISTS device_group(
            group_num             VARCHAR(30)  PRIMARY KEY,
            group_name      VARCHAR(30),
            description     VARCHAR(50),
            time_create     VARCHAR(30),
            time_update     VARCHAR(30)
        )
        """

        sql3 = """CREATE TABLE IF NOT EXISTS relation(
            id          VARCHAR(30) PRIMARY KEY,
            group_num       VARCHAR(30)
        )
        """
        self.cursor.execute(sql1)
        self.cursor.execute(sql2)
        self.cursor.execute(sql3)
        
    def _reconn(self):
        pass
        try:
            self.db.ping(reconnect=False)
        except Exception as e:
            self.db = pymysql.connect(host= self._host,user= self._user,passwd= self._password)
            self.cursor = self.db.cursor(cursor=DictCursor)  
            self.cursor.execute(f"USE {self._database}")

    def add_device(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                # self.cursor.execute("SELECT * FROM device WHERE id={id}".format(id=x["id"]))
                # if self.cursor.fetchone != None:
                #     self.cursor.execute("DELETE FROM device WHERE id={id}".format(id=x["id"]))
                #     self.cursor.execute("DELETE FROM relation WHERE id={id}".format(id=x["id"]))
                sql1 = f"""INSERT INTO device(
                    id,name,type,state,
                    auth_salt,auth_secret,time_register,time_update,
                    hardware_sn,hardware_model,
                    software_base_version,software_base_lastUpdate,software_base_status,
                    software_work_version,software_work_lastUpdate,software_work_status,
                    nic_eth_mac,nic_eth_ipv4,nic_wifi_mac,nic_wifi_ipv4,
                    LTE_IMEI 
                ) VALUES (
                    '{x["id"]}','{x["name"]}','{x["type"]}','{x["state"]}',
                    '{x["auth"]["salt"]}','{x["auth"]["secret"]}','{x["time"]}','{x["time"]}',
                    '{x["hardware"]["sn"]}','{x["hardware"]["model"]}','{x["software"]["base"]["version"]}','{x["software"]["base"]["lastUpdate"]}',
                    '{x["software"]["base"]["status"]}','{x["software"]["work"]["version"]}','{x["software"]["work"]["lastUpdate"]}','{x["software"]["work"]["status"]}',
                    '{x["nic"]["eth"]["mac"]}','{x["nic"]["eth"]["ipv4"]}','{x["nic"]["wifi"]["mac"]}','{x["nic"]["wifi"]["ipv4"]}',
                    '{x["LTE_IMEI"]}'
                )
                """
                self.cursor.execute(sql1)
            self.db.commit()
        except Exception as e:
            print(e)
            message = str(e)
            self.flag = False
            self.db.rollback()
            return message

    def del_device(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                sql1 = f"DELETE FROM device WHERE id='{x}'"
                sql2 = f"DELETE FROM relation WHERE id='{x}'"
                self.cursor.execute(sql1)
                self.cursor.execute(sql2)
            self.db.commit()
        except Exception as e:
            print(e)
            message = str(e)
            self.flag = False
            self.db.rollback()
            return message

    def update_device(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                val = ""
                tmp1:dict = x
                tmp2 = {}
                tmp1.pop("id")
                tmp1.pop("time")
                dd(tmp2,"",tmp1)
                for key in tmp2:
                    val = val+f"{key}={tmp2[key]},"
                val = val+"time_update = '{}'".format(x["time"])
                sql = "update device SET "+val+" WHERE id='{}'".format(x["id"])
                self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            message = str(e)
            self.flag = False
            self.db.rollback()
            return message
    
    def get_device_by_id(self,data:list):
        self._reconn()
        self.flag = True
        res = []
        for x in data:
            sql = "SELECT * FROM device WHERE id='{}'".format(x)
            self.cursor.execute(sql)
            tmp = self.cursor.fetchone()
            if tmp == None:
                continue
            tmp = du(tmp)
            res.append(tmp)
        return res
        
    def get_device_by_group(self,data:list):
        self._reconn()
        self.flag = True
        res = []
        for x in data:
            sql = "SELECT a.*, b.group_num FROM device a join relation b ON a.id = b.id WHERE b.group_num = '{}'".format(x)
            self.cursor.execute(sql)
            tmp = self.cursor.fetchall()
            for x in tmp:
                res.append(du(x))
        return res
    
    def get_all_device(self):
        self._reconn()
        self.flag = True
        self.cursor.execute("SELECT * FROM device")
        res = []
        tmp = self.cursor.fetchall()
        for x in tmp:
            res.append(du(x)) 
        return res
    
    def get_device_and_group_by_id(self,data:list):
        self._reconn()
        self.flag = True
        res = []
        for x in data:
            sql = """SELECT a.*, c.group_name, c.description 
              FROM device a LEFT JOIN relation b ON a.id = b.id LEFT JOIN device_group c ON b.group_num=c.group_num 
              WHERE a.id = '{}'""".format(x)
            self.cursor.execute(sql)
            tmp = self.cursor.fetchone()
            if tmp == None:
                return res
            res.append(du(tmp))
        return res
    
    def get_all_device_and_group(self):
        self._reconn()
        self.flag = True
        sql = """SELECT a.*, c.group_name, c.description 
              FROM device a LEFT JOIN relation b ON a.id = b.id LEFT JOIN device_group c ON b.group_num=c.group_num"""
        self.cursor.execute(sql)
        res = []
        tmp = self.cursor.fetchall()
        for x in tmp:
            print(du(x))
            res.append(du(x))
        return res

    
    def add_group(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                sql = f"""INSERT INTO device_group(group_num,group_name,description,time_create,time_update) 
                    VALUES('{x["group_num"]}','{x["group_name"]}','{x["description"]}','{x["time"]}','{x["time"]}')"""
                self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message
    
    def del_group(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                self.cursor.execute(f"SELECT * FROM relation WHERE group_num='{x}'")
                if self.cursor.fetchone() == None:
                    sql1 = f"DELETE FROM device_group WHERE group_num='{x}'"
                    self.cursor.execute(sql1)    
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message
            
    def update_group(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                val = ""
                for key in x:
                    if key == "group_num" or key == "time":
                        continue
                    val = val+f"""'{key}'='{x[key]}',"""
                val = val+"time_update = '{}'".format(x["time"])
                sql = "update device_group SET "+val+" WHERE id='{}'".format(x["id"])
                self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message
    
    def get_all_group(self):
        self._reconn()
        self.flag = True
        self.cursor.execute("SELECT * FROM device_group")
        res = []
        tmp = self.cursor.fetchall()
        for x in tmp:
            res.append(du(x))
        return res

    def get_group(self,data:list):
        self._reconn()
        self.flag = True
        res = []
        for x in data:
            sql = "SELECT * FROM device_group WHERE group_num='{}'".format(x)
            self.cursor.execute(sql)
            res.append(self.cursor.fetchone())
        return res
    

    def add_relation(self,data:list):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                sql = """INSERT INTO relation(id,group_num) VALUES('{}','{}')""".format(x["id"],x["group_num"])
                self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message
    
    def del_relation(self,data):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                sql1 = "DELETE FROM relation WHERE id='{}'".format(x)
                self.cursor.execute(sql1)    
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message
    
    def update_relation(self,data):
        self._reconn()
        self.flag = True
        try:
            for x in data:
                sql = "update device_group SET group_num='{}' WHERE id='{}'".format(x["group_num"],x["id"])
                self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.flag = False
            print(e)
            message = str(e)
            self.db.rollback()
            return message