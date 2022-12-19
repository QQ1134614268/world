import pymongo

from config.env_default import MONGO_HOST, MONGO_PORT


def create_mongo_db():
    client = pymongo.MongoClient(host="mongodb://{}:{}/".format(MONGO_HOST, MONGO_PORT))
    # 指定数据库
    db = client.world
    # db = client["world"]
    return db


mongoDB = create_mongo_db()

if __name__ == '__main__':
    # collection = mongoDB.student
    # collection = mongoDB["book"]
    collection = mongoDB.book
    collection.insert_one({"name": 5, "price": 2})
    # data = collection.find_one({"name":1})
    data = list(collection.find({}))
    print(data)
