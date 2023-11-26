import logging
import logging.config
from os import path, listdir
import time

def getFilename(logtype: str) -> str:
    """用于生成对应文件类型和时间的文件名"""
    t = time.localtime()
    filename = "{}-{}-{}_{}.log".format(t.tm_year,t.tm_mon,t.tm_mday,logtype)
    return filename


def getAllLogs(file: str) -> list:
    """返回对应类型的所有日志内容"""
    j: list = []
    path = "./logging/logs"
    for filename in listdir(path):
        if file in filename:
            print(filename)
            tempdict: dict = {}
            tempdict["time"] = filename.split('_')[0]
            with open(path+'/'+filename,'r') as f:
                tempdict["data"] = f.readlines()
            j.append(tempdict)
    return j


def loggingQuery(j: dict) -> list:
    """根据请求查询对应类型的日志"""
    logtype = j["logtype"]
    if logtype == "deviceLogin":
        res = getAllLogs("loginStatus")
    elif logtype == "heartbreak":
        res = getAllLogs("hbReport")
    elif logtype == "database":
        res = getAllLogs("dbOperate")
    return res


def loggingUpload(j: dict) -> list:
    """根据请求写入对应类型的日志"""
    logtype = j["logtype"]

    if logtype == "deviceLogin":
        loginStatusUpload(j["data"])
    elif logtype == "heartbreak":
        hbReportUpload(j["data"])
    elif logtype == "database":
        dbOperateUpload(j["data"])

    return []


def loginStatusUpload(data: dict):
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logconf.ini')
    logging.config.fileConfig(fname=log_file_path, defaults={'filename': getFilename("loginStatus")})
    logger = logging.getLogger("loginStatus")

    if "status" in data:
        if data["status"] == 0:
            logger.info("{} - {}".format(data["msg"], data["id"]))
        elif data["status"] == -1:
            logger.error("{} - {}".format(data["msg"], data["id"]))
    else:
        logger.info("{} - {}".format(data["msg"], data["id"]))

def hbReportUpload(data: dict):
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logconf.ini')
    logging.config.fileConfig(fname=log_file_path, defaults={'filename': getFilename("hbReport")})
    logger = logging.getLogger("hbReport")

    id = data.pop("id")

    print(data)

    info = ""
    for k,v in data.items():
        print("{}: {};".format(k,v))
        info += "{}: {};".format(k,v)

    logger.info("{} - {}".format(info, id))


def dbOperateUpload(data: dict):
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logconf.ini')
    logging.config.fileConfig(fname=log_file_path, defaults={'filename': getFilename("dbOperate")})
    logger = logging.getLogger("dbOperate")
    
    logger.info(data["msg"])
