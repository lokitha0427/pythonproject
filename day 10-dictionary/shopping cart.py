cart={}
while True:
    ch=int(input("1.Add items 2.Remove items 3.update items 4.view cart"))
    if ch==1:
        id=input("Enter the ID:")
        item=input("Enter the product name:")
        price=int(input("Enter the price:"))
        quantity=int(input("Enter the quantity"))
        cart.setdefault(id,[item,price,quantity])
        print("Product stored successfully")
    elif ch==2:
         id=input("Enter the ID:")
         del(cart[id])
    elif ch==3:
        id=input("Enter the ID:")
        item=input("Enter the product name:")
        price=int(input("Enter the price:"))
        quantity=int(input("Enter the quantity"))
        cart[id]=([item,price,quantity])
    else:
        for id in cart.keys():
            print(id," ",cart[id][0]," ",cart[id][1]," ",cart[id][2])
            
print(cart)
