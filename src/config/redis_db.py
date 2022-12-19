# -*- coding:utf-8 -*-
import redis

from config.env_default import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD


def create_redis_db():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD,
                             decode_responses=True)


redisDB = create_redis_db()

if __name__ == '__main__':
    redisDB.set("name", "中国")
    print(redisDB.get("name"))
