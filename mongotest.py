import pymongo
client = pymongo.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"yash vij",
    "email" : "yashivj@gmail.com",
    }
d = {
    "name":"yash vij",
    "email" : "yashivj@gmail.com",
    }
d = {
    "name":"yash vij",
    "email" : "yashivj@gmail.com",
    }
d = {
    "name":"yash vij",
    "email" : "yashivj@gmail.com",
    }
d = {
    "name":"yash vij",
    "email" : "yashivj@gmail.com",
    }

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)


