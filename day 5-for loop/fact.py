#for loop
#factorial
n=int(input("enter"))
fact=1
for i in range(1,n+1):
        fact=fact*i
        if i<n:
                print(f"{i}*",end="")
        elif i==n:
           print(f"{i}",end="")
print(f"={fact}")
