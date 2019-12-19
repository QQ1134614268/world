import jwt
import time

secret = 'secret'  # 配置文件


def get_token(payload):
    return str(jwt.encode(payload, secret, algorithm='HS256'), "utf_8")


def get_payload(jwt_token):
    return jwt.decode(bytes(jwt_token, "utf_8"), secret, algorithms=['HS256'])


if __name__ == '__main__':
    temp_user = {"name": "w&g", "id": 1, "timestamp": int(time.time())}
    jwt_token = get_token(temp_user)
    print(jwt_token)
