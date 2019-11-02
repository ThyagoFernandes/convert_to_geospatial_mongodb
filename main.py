
import random
import sys
import time
import pip
import pymongo  
from pymongo import  GEO2D


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dataset"]

col = db["restaurants"]
respo = {}
respo1 = {"address.location":{"$exists": "true"}}
if(col.count_documents(respo) != col.count_documents(respo1)):
   print(col.count_documents(respo)!=col.count_documents(respo1) )
   for r in col.find({}):
      try:
         col.update_one ({"restaurant_id":r['restaurant_id']},{"$set":{"address.location":{'type':"Point",'coordinates':[
         r["address"]["coord" ][0],r["address"]["coord" ][1]]}}})
      except:
         col.update_one ({"restaurant_id":r['restaurant_id']},{"$set":{"address.location":{'type':"Point",'coordinates':[
         -0.111111111,0.111111111]}}})
col.create_index([ ("address.location", "2dsphere") ])
r = col.find({"address.location":{"$near":{"$geometry":{ "type": "Point", "coordinates": [-73.9903, 40.7570] }, "$minDistance": 0, "$maxDistance": 1000 }}})
print(r.count())
   
   


