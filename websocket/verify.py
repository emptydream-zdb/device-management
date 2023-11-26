import jwt
import time
from hashlib import sha256

"""
    status  状态
      0     正常
     -1   密码错误
     -2   用户不存在
     -3  token解析失败
"""

salt = "asdghiuwhg"         # 随机的salt密钥

def generateToken(id: str) -> str:
    """根据设备id生成token"""
    tokenExporeTime = 300 # token有效时间:300s
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }                           # 设置headers，即加密算法的配置
    exp = int(time.time() + tokenExporeTime)  # 设置超时时间：当前时间的100s以后超时
    payload = {
        "id": id,
        "exp": exp
    }                           # 配置主体信息

    token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers)   # 生成token
    
    return token


def verifyToken(id: str, token: str) -> bool:
    """验证用户token"""
    try:
        payload = jwt.decode(token, salt, algorithms=['HS256'],verify=False)
    except jwt.exceptions.ExpiredSignatureError:
        return False

    if id == payload["id"]:
        return True
    else:
        return False
    

def pwdComp(data: dict, recv: dict) -> dict:
    """密码密文比对"""
    """
        接受json格式：
        {
            "id": ...,
            "password": ...
        }
    """
    salt = data["auth"]["salt"]
    hash=sha256((recv["id"]+recv["password"]+salt).encode()).hexdigest()

    if recv["id"] == data["id"]:
        if hash == data["auth"]["secret"]:
            return {
                "status": 0,
                "msg": "ok"
            }
        else:
            return {
                "status": -1,
                "msg": "password error"
            }
    else:
        return {
            "status": -2,
            "msg": "id does not exist"
        }
