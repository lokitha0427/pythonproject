mul=1
for i in range(1,11,1):
    mul=mul*i
    if i>1 and i<=11:
       print(f"*{i}",end="")
    else:
        print(f"{i}",end="")
print(f"={mul}")
