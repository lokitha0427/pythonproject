#for loop
#sum of series

n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
    if i<n:
           print(f"{i}+",end="")
    elif i==n:
        print(f"{i}",end="")
print(f"={sum}")
    
    
