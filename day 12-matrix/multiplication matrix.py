#multiply matrix
a=[]
b=[]
c=[]
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(int(input()))
for i in range(2):
    b.append([])
    for j in range(2):
        b[i].append(int(input()))
for i in range(2):
    c.append([])
    for j in range(2):
        c[i].append(a[i][j]*b[i][j])
for k in c:
    print(k)
