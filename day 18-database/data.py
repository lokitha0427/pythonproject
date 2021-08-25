#name=input("enter the name:")
#cost=int(input("cost:"))
#qty=int(input("quantity:"))
import pymongo
con=pymongo.MongoClient("mongodb://localhost:27017")
db=con["Hotel"]
col=db["Menu"]

for i in col.find().sort("cost").limit(2):
    print(f"{i['name']} {i['cost']}")



for i in col.find().sort("cost",-1).limit(1):
    print(f"{i['name']} {i['cost']}")

