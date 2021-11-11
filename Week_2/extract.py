import pymongo
from pymongo import MongoClient
import pandas as pd

connection=MongoClient('localhost',27017)
db=connection.EmployeeDB
data=db.employees
Employeelist=data.find()
for item in Employeelist:
    print("Name:"+item["name"]+" "+"Dept:"+item["dept"])

df=pd.DataFrame(list(data.find()))
print(df)