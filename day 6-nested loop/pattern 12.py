#pattern 12
'''
 1  6 11 16 21 
 2  7 12 17 22 
 3  8 13 18 23 
 4  9 14 19 24 
 5 10 15 20 25 
'''
for i in range(1,6):
    z=i
    for j in range(1,6):
        if z<10:
            print(" "+str(z),end=" ")
        else:
            print(z,end=" ")
        z=z+5
    print() 
