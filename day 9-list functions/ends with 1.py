#display the number ends with 1
size=int(input())
x=[]
for i in range(size):
    x.append(int(input()))
print("element ends with 1")
for i in x:
    if i%10==1:
        print(i)
        
