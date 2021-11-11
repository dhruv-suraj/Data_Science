class Seller:
    def __init__(self):
        self.product_quantity={}
        self.product_price={}
        self.profit=0
    
    def update(self):
        item_name=input("Enter item name:")
        item_quantity=int(input("Enter item quantity:"))
        item_price=int(input("Enter selling price:"))
        self.product_quantity[item_name]=item_quantity
        self.product_price[item_name]=item_price

    def show(self):
        print("Show items")
        for i,j in self.product.items():
            print(i,j)
    
    def buy(self,item_name,quantity):
        if quantity>self.product_quantity.get(item_name):
            print("Item outofstock")
        else:
            self.product_quantity[item_name]=self.product_quantity.get(item_name)-quantity
            self.profit+=self.product_price.get(item_name)+quantity

class Buyer:
    def __init__(self):
        self.cart={}
        self.quantity={}
        self.total_amount=0

    def search(self,seller,item_name):
        if seller.product_quantity.get(item_name):
            print("Quantity"+str(seller.product_quantity.get((item_name))))
            print("Price per quantity"+str(seller.product_price.get(item_name)))
            choice=input("Do you want to add this to your cart y/n?")
            if choice=="y":
                quantity=int(input("Enter quantity"))
                if quantity>seller.products_quantity.get(item_name):
                    print("quantity is to much")
                    self.search(seller.item_name)
                else:
                    self.cart[item_name]=seller.product_price.get(item_name)*quantity
                    self.quantity[item_name]=quantity
                    self.total_amount+=seller.product_price.get(item_name)*quantity
            else:
                pass
        else:
            print("item not found")

    def show(self):
        print("Show items")
        for i,j in self.cart.items():
            print(i,j)
    
    def buy(self,seller):
        print("These are the items in your cart...")
        self.show()
        for item,quantity in self.quantity.items():
            seller.buy(item.quantity)

seller=Seller()
buyer=Buyer()    
while True:
    choice=input("Are you buyer or seller? b/s:")
    if choice=="s":
        while True:
            print("1: Update items")
            print("2: Show items")
            print("4: Exit")
            choice = input("Enter your choice:")
            if choice == "1":
                seller.update()
            elif choice == "2":
                seller.show()
            elif choice == "3":
                option=False
            else:
                print("Invalid choice")
    elif choice=="b":
        while True:
            print("1: Search items")
            print("2: Buy items")
            print("4: Exit")
            choice = input("Enter your choice:")
            if choice == "1":
                item_name=input("Enter name of product:")
                buyer.search(seller.item_name)
            elif choice == "2":
                buyer.buy(seller)
            elif choice == "3":
                option=False
            else:
                print("Invalid choice")

    else:
        print("invalid choice")