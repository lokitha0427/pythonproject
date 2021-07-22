#print s shape in matrix
x=[]
r=int(input("Enter the row value:"))
c=int(input("Enter the column value:"))
for i in range(r):
    x.append([])
    for j in range(c):
        x[i].append(int(input()))
for i in range(r):
    for j in range(c):
        if ((i==0 or i==2 or i==4) and (j>0 and j<4)):
            print(" "+str(x[i][j]),end="")
        elif ((j==0) and (i>0 and i<2)):
            print(" "+str(x[i][j]),end="")
        elif ((j==4) and (i>2) and i<4):
            print(" "+str(x[i][j]),end="")
        else:
            print(" ",end=" ")
    print()

