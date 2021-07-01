n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
    if i>1 and i<=n:
           print(f"+{i}",end="")
    else :
        print(f"{i}",end="")
print(f"={sum}")
    
    
