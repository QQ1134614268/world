# -*- coding:utf-8 -*-
import redis

from global_variable import REDIS_HOST, REDIS_PORT


def create_redisDB():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


redisDB = create_redisDB()

if __name__ == '__main__':
    redisDB.set("name", "中国")
    print(redisDB.get("name"))
