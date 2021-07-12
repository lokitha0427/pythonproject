#sum of element in the list
size=int(input())
x=[]
sum=0
for i in range(size):
    x.append(int(input()))
    sum+=x[i]
print(sum)
