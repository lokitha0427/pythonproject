f=open("stock.txt")
id=int(input("Enter the ID:"))
for i in f:
    if str(id) in i:
        j=i.split(" ")
        print(f"Name: {j[1]}")
        print(f"Price: {j[2]}")
        Qty=int(input("Quantity:"))
        if Qty<=int(j[3]):
            print(f"Total Amount={Qty*int(j[2])}")
        else:
            print("out of stock")
            break
else:
    print("Invalid ID")