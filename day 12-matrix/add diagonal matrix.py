#transpose matrix
a=[[1,2],[3,4]]
b=[[0,0],[0,0]]
for i in range(a):
    for j in range(b):
        b[i][i]+=a[i][j]
for k in b:
    print(k)
