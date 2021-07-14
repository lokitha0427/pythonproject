#online shopping
product={101:["kitkat",10,5],102:["Dm,20,50"],103:["Milky bar",30,20],104:["Perk",40,30],105:["Munch,50,30"]}
sum=0
while True:
    id=int(input("Enter the product ID:"))
    if id in product:
        print("Product name:",product[id][0])
        print("price:",product[id][1])
        quantity=int(input("Enter the quantity:"))
        if quantity<product[id][2]:
            amount=quantity*product[id][2]
            print("Amount is:",amount)
            sum+=amount
            print("Successfully purchased")
        else:
            print("stock unavailable")
    else:
        print("ID unavailable")
        break
print("Bill amount",sum)
