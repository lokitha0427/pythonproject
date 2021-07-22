#subtraction matrix
a=[[56,89],[23,48]]
b=[[33,42],[47,96]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]-b[i][j]
for k in c:
    print(k)
