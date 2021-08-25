name=input("Name:")
course=input("Course name:")
course_fee=int(input("Course fee:"))
paid_amount=int(input("Amount paid:"))
due_amount=course_fee-paid_amount
print("Due Amount:",due_amount)
import pymongo
con=pymongo.MongoClient("mongodb://localhost:27017")
db=con["Student"]
col=db["Payment"]
col.insert_one({"name":name,"course":course,"course fee":course_fee,"paid amount":paid_amount,"due amount":due_amount})
print("Student detail saved successfully")
#col.update_one({"name":"lokitha"},{"$set":{"paid amount":15000}})
#print("updated successfully")













col.delete_one({"name":"lokitha"})
print("deleted successfully")