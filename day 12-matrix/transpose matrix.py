a=[[1,2],[3,4]]
b=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i]=a[i][j]
for k in b:
    print(*k)