#diff btw largest and smallest values in the list
size=int(input())
x=[]
for i in range(size):
    x.append(int(input()))
for i in x:
    a=max(x)-min(x)
print(a)


