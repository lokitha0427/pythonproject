prod1=input("enter the product name")
pr1=int(input("enter the price"))
qty1=int(input("enter the quanlity"))
dis1=float(input("enter the discount"))
total1=qty1*pr1
discount1=total1-(total1*dis1)
net_discnt1=total1-discount1

prod2=input("enter the product name")
pr2=int(input("enter the price"))
qty2=int(input("enter the quanlity"))
dis2=float(input("enter the discount"))
total2=qty2*pr2
discount2=total2-(total2*dis2)
net_discnt2=total2-discount2


prod3=input("enter the product name")
pr3=int(input("enter the price"))
qty3=int(input("enter the quanlity"))
dis3=float(input("enter the discount"))
total3=qty3*pr3
discount3=total3-(total3*dis3)
net_discnt3=total3-discount3

prod4=input("enter the product name")
pr4=int(input("enter the price"))
qty4=int(input("enter the quanlity"))
dis4=float(input("enter the discount"))
total4=qty4*pr4
discount4=total4-(total4*dis4)
net_discnt4=total4-discount4

prod5=input("enter the product name")
pr5=int(input("enter the price"))
qty5=int(input("enter the quanlity"))
dis5=float(input("enter the discount"))
total5=qty5*pr5
discount5=total5-(total5*dis5)
net_discnt5=total5-discount5

total_amount=total1+total2+total3+total4+total5
discount_amount=net_discnt1+net_discnt2+net_discnt3+net_discnt4+net_discnt5
pay_amount=total_amount-discount_amount
print(f"total amount {total_amount}")
print(f"discount {discount_amount}")
print(f"Pay amount {pay_amount}")








'''
prd1,prd2,prd3,prd4,prd5=input("enter the five products")
pr1,pr2,pr3,pr4,pr5=int(input("enter the price"))
qnty1,qnty2,qnty3,qnty4,qnty5=int(input("enter the quantity"))
discount=int(input("enter the discount"))
total=qnty1,qnty2,qnty3,qnty4,qnty5*qnty1,qnty2,qnty3,qnty4,qnty5
totalamount=total
payamount=totalamount-discount
print(f"total amount {totalamount}")
print(f"discount {discount}")
print(f"payamount {payamount}")
'''

