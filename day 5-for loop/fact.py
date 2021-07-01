#for loop
#factorial
n=int(input("enter"))
fact=1
for i in range(1,n+1):
        fact=fact*i
        if i>1 and i<=n:
                print(f"*{i}",end="")
        else:
           print(f"{i}",end="")
print(f"={fact}")
