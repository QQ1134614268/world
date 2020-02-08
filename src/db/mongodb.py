import pymongo


def create_mongoDB():
    client = pymongo.MongoClient(host="mongodb://127.0.0.1:27017/")
    # 指定数据库
    db = client.world
    # db = client["world"]
    return db


db = create_mongoDB()

if __name__ == '__main__':
    # collection = db.student
    # collection = db["book"]
    collection = db.book
    collection.insert_one({"name": 5, "price": 2})
    # data = collection.find_one({"name":1})
    data = list(collection.find({}))
    print(data)
