#count the odd number
size=int(input())
x=[]
count=0
for i in range(size):
    x.append(int(input()))
    if x[i]%2==1:
        count+=1
print(count)
