#print T shape in matrix
x=[]
r=int(input("Enter the row value:"))
c=int(input("Enter the column value:"))
for i in range(r):
    x.append([])
    for j in range(c):
        x[i].append(int(input()))
for i in range(r):
    for j in range(c):
        if ((j==0 or j==4) or (i==j)):
            print(" "+str(x[i][j]),end="")
        else:
            print(" ",end=" ")
    print()

