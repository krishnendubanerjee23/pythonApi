from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

@app.route('/abc',methods=['GET', 'POST'])
def test():
    if(request.method=='POST'):

        client = pymongo.MongoClient("mongodb+srv://krishnendubanerjee23:Kolkata1@cluster0.7ju5nnf.mongodb.net/?retryWrites=true&w=majority")
        db = client.MangoApi

        data = {
            "item": request.json['item1'],
            "qty": request.json['qty1'],
            "size": {"h": request.json['hight'], "w": request.json['Weight'], "uom": request.json['volum']},
            "status": request.json['status']
            }

        db1 = client['API']
        collections = db1['MangoApi']
        collections.insert_one(data)

        return jsonify((print(db)))

if __name__ == '__main__':
    app.run()
