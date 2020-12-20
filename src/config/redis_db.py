# -*- coding:utf-8 -*-
import redis

from config.conf import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB


def create_redisDB():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD,
                             decode_responses=True)


redisDB = create_redisDB()

if __name__ == '__main__':
    redisDB.set("name", "中国")
    print(redisDB.get("name"))
