#sum of largest and smallest number in the list
size=int(input())
x=[]
for i in range(size):
    x.append(int(input()))
print("sum of max and min value is")
for i in x:
    a=min(x)+max(x)
print(a)
