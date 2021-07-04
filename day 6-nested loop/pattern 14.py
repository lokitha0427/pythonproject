#pattern 14
'''
'''
for i in range(5,0,-1):
    z=i
    for j in range(5,0,-1):
        if z<10:
            print(" "+str(z),end=" ")
        else:
            print(z,end=" ")
        z=z+5
    print()
