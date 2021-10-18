x=int(input("Enter price of 1st number:"))
y=int(input("Enter price of 2nd number:"))

add= x+y
tax=add*0.1
total=add+tax
if(total>=1000):
    total=total-total*0.1
elif(total>=500 and total<=1000):
    total=total-total*0.7
else:
    pass
print(total)

li=["Milk","Chocolates"]