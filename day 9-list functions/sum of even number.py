#sum of even number in the list
size=int(input())
x=[]
sum=0
for i in range(size):
    x.append(int(input()))
    if x[i]%2==0:
        sum+=x[i]
print(sum)
