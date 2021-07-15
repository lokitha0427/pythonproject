name=input("Enter your name:")
count=0
for i in name:
    if i in "aeiouAEIOU":
        count+=1
print(count)
