from fastapi import FastAPI,Path
from typing import  Optional
app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# @app.get("/about")
# def about():
#     return {"About":"Dhruv"}
inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "amul"
    }
}
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(test: int,name: Optional[str]=None):
    for item_id in inventory:
        return inventory[item_id]
    return {"Data": "Not found"}
# #http://127.0.0.1:8000/get-by-name?name=Milk
#
#
#
# class Seller:
#     def __init__(self):
#         self.product.quantity={}
#         self.product.price={}
#         self.profit=0
#
#     def update(self):
#         item_name=input("Enter name:")
#         item_quantity=int(input("Enter item quantity"))
#         item_price = int(input("Enter item price"))
#         self.product_quantity[item_name]=item_quantity
#         self.product_price[item_name]=item_price
#
#     def show(self):
#         print("Show items...")
#         for i,j in self.product_quantity.items():
#             print(i,j)
#
#     def buy(self,item_name,quantity):
#         if quantity>self.product_quantity.get(item_name):
#             print("quantity not found")
#         else:
#             self.product_quantity[item_name]=self.product_quantity.get(item_name)-quantity
#             self.profit+=self.product_price.get(item_name)*quantity
#
# class Buyer:
#     def __init__(self):
#         self.cart={}
#         self.quantity={}
#         self.total_amount={}
#
#     def search(self,seller,item_name):
#         if seller.product_quantity.get(item_name):
#             print()
