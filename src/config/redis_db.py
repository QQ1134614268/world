# -*- coding:utf-8 -*-
import redis

from config.env_default import world_env


def create_redis_db():
    return redis.StrictRedis(host=world_env.redis_host, port=world_env.redis_port, db=world_env.redis_db,
                             password=world_env.redis_password, decode_responses=True)


redisDB = create_redis_db()

if __name__ == '__main__':
    redisDB.set("name", "中国")
    print(redisDB.get("name"))
