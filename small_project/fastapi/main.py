from fastapi import FastAPI,Path
from typing import  Optional
app = FastAPI()

class Item():
    name:str
    price:float
    brand:Optional[str]=None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# @app.get("/about")
# def about():
#     return {"About":"Dhruv"}

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(test: int,name: Optional[str]=None):
    for item_id in inventory:
        return inventory[item_id]
    return {"Data": "Not found"}
# #http://127.0.0.1:8000/get-by-name?name=Milk

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return{"Error":"Item Id already exists"}
        
    inventory[item_id]=item
    return inventory[item_id]