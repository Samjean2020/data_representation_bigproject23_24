# import the Flask class.
from flask import Flask, url_for, request, redirect, abort, jsonify
# create an instance of the above class.
app = Flask(__name__, static_url_path='', static_folder='staticpages')
# use the root() decorator.
@app.route('/')
# create a function.
def index():
    # return an HTML content-type.
    # http://127.0.0.1:5000  or curl http://127.0.0.1:5000
    return "UN Women Gender and Covid-19 Survey Report 2022."

# Step 1 Get All using the getAll()function.
# curl http://127.0.0.1:5000/GCdata.
# GCdata means gendered data.
@ app.route('/GCdata')
def get_All():
    return "served by Get_All()"

# curl http://127.0.0.1:5000/GCdata/1
@ app.route('/GCdata/<int:id>')
def findBy(id):
    return"served by findBy id with it "+str(id)

# Step 2 Create using the POST() method.
# curl -X POST http://127.0.0.1:5000/GCdata/2
@ app.route('/GCdata', methods = ["POST"])
def create():
    return "served by Create"
# Step 3 Update using the PUT()attribute.
# curl -X PUT http://127.0.0.1:5000/GCdata/3
@ app.route('/GCdata/<int:id>', methods = ["PUT"])
def update(id):
    return "served by update with it" + str(id)

# Step 4 Delete or remove using the DELETE() method.
# curl - X DELETE  http://127.0.0.1:5000/GCdata/4
@ app.route('/GCdata/<int:id>', methods = ["DELETE"])
def delete(id):
    return "served by delete with it" + str(id)

# Write code for each of CRUD operations.
# Make an array of data from UN Women database.
# Use index of each data entry as id, instead of their proper id, as some of them are not integer-type.
GCdataset=[{"id":0, "Country":"Indonesia","Sexe":"Male", "Age": 43},    
{"id":1, "Country":"Indonesia","Sexe":"Female", "Age": 47},                      
{"id":4350, "Country":"Kiribati", "Sexe": "Female", "Age": 35},
{"id":4351, "Country":"Kiribati", "Sexe": "Female", "Age": 19},                            
{"id":5550, "Country":"Pakistan", "Sexe": "Female", "Age": 55},
{"id":5551, "Country":"Pakistan", "Sexe": "Male", "Age":23},                    
{"id":8370, "Country":"PNG(Papua New Guinea)","Sexe":"Female", "Age":21},
{"id":8371, "Country":"PNG(Papua New Guinea)","Sexe":"Male", "Age": 34},          
{"id":11990, "Country":"Samoa","Sexe":"Male", "Age":53},
{"id":11991, "Country":"Samoa","Sexe":"Male", "Age": 32},                    
{"id":13993, "Country":"Solomon Island", "Sexe": "Male", "Age":32},
{"id":13994, "Country":"Solomon Island", "Sexe": "Female", "Age":26},          
{"id":17840, "Country":"Tonga", "Sexe": "Female", "Age": 75},          
{"id":17841, "Country":"Tonga", "Sexe": "Female", "Age": 40}]

# number of CRUD operations.
nextId=4
# getAll.
# curl http://127.0.0.1:5000/GCdataset
@ app.route('/GCdataset')
def getAll():
    return jsonify(GCdataset)

# find by id.
# curl http://127.0.0.1:5000/GCdataset/1

@ app.route('/GCdataset/<int:id>')
def find_By(id):
    foundData=list(filter(lambda t:t["id"] == id, GCdataset))
    if len (foundData) == 0:
        return jsonify ({}, 204)
    return jsonify(foundData[0])
     
# create
#  curl -X POST -H "Content-type:application/json" -d "{\"Country\": \"Papua New Guinea\", \"Sexe\": \"Male\", \"Age\":40}" http://127.0.0.1:5000/GCdataset/2
@ app.route('/GCdataset',methods=["POST"])
def CreateD():
    global nextId
    if not request.json:
        abort(400)
    dataset={
        "id":nextId,
        "Country":request.json["Country"],
        "Sexe":request.json["Sexe"],
        "Age":request.json["Age"]
        }
    GCdataset.append(dataset)
    nextId+=1
    return jsonify(dataset)

#update
# curl -X PUT -H "Content-type:application/json" -d "{\"Country\": \"Papua New Guinea\", \"Sexe\": \"Male\", \"Age\":40}" http://127.0.0.1:5000/GCdataset/3
@app.route('/GCdataset/<int:id>',methods=['PUT'])
def up_date(id):
    foundData=list(filter(lambda t: t["id"] == id, GCdataset))
    if len(foundData) == 0:
        return jsonify({}), 404
    currentdataset=foundData[0]
    if 'Country' in request.json:
        currentdataset['Country']=request.json['Country']
    if 'Age' in request.json:
        currentdataset['Age']=request.json['Age']
    if 'Sexe' in request.json:
        currentdataset['Sexe']=request.json['Sexe']
    return jsonify(currentdataset)

# delete
# curl -X DELETE http://127.0.0.1:5000/GCdataset/4
@ app.route('/GCdataset/<int:id>',methods= ["DELETE"])
def Delete(id):
    foundData=list(filter(lambda t:t["id"]==id, GCdataset))
    if len (foundData)==0:
        return jsonify ({}), 404
    GCdataset.remove(foundData[0])
    return jsonify ({"done":True})

if __name__ == "__main__":
    app.run(debug= True)

