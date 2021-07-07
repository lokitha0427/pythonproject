n=int(input("enter the number"))
sum=0
t=n
while t>0:
    fact=1
    digit=t%10
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    t//=10
if(sum==n):
    print("the given number is a strong number")
else:
    print("the given number is not a strong number")
