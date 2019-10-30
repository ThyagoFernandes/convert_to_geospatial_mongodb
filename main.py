
import random
import sys
import time
import pip
import pymongo  


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]

col = db["restaurants"]
respo = col.find({})
col.update_many({},{'$unset':{'val1':"",'val2':""}})

i = 0
for r in respo:
   col.update_one ({"restaurant_id":r['restaurant_id']},{"$set":{"address.coord":{"type":"Point","coordinates":r["address"]["coord" ]}}})
   
   


