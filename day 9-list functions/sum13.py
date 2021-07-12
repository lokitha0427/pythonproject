#sum13
x=[1,2,13,1]
count=0
i=0
while i<len(x):
    if x[i]!=13:
        count=count+x[i]
        i=i+1
print(count)
