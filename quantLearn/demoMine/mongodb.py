#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

dblist = myclient.list_database_names()
print(dblist)
if "test" in dblist:
  print("数据库已存在！")