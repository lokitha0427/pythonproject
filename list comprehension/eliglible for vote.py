#list comprehension
#eligible for vote
a=[3,56,12,34,19,2]
b=[f"{i}-eligible" if(i>18) else f"{i}-not eligible" for i in a]
print(b)
