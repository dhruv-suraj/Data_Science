data = {}
def update(data):
    item_name=input("Enter item name:")
    item_quantity=input("Enter item quantity:")
    data[item_name]=item_quantity
def show(data):
    print("Show items")
    for i,j in data.items():
        print(i,j)
def search(data,key):
    return data.get(key)
while True:
    print("1: Update items")
    print("2: Show items")
    print("3: Search")
    print("4: Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        update(data)
    elif choice == "2":
        show(data)
    elif choice == "3":
        key=input("Enter the item to be searched")
        print(search(data,key))
    elif choice == "4":
        option=False
    else:
        print("Invalid choice")