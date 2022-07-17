import pymongo
client = pymongo.MongoClient("mongodb+srv://krishnendubanerjee23:Kolkata1@cluster0.7ju5nnf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Krishnendu",
    "email" : "krishnendubanerjee23@gmail.com",
    "surname" : "banerjee"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
