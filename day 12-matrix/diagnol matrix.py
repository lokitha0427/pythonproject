a=[[1,2,3],[1,2,3],[1,2,3]]
sum=0
for i in range(3):
    for j in range(3):
        if(i==j):
            sum=sum+a[i][j]
        elif(i+j==2):
            sum=sum+a[i][j]
print(sum)