#even number
'''
 2  4  6  8 10 
12 14 16 18 20 
22 24 26 28 30 
32 34 36 38 40 
42 44 46 48 50 
'''
k=2
for i in range(5):
    for j in range(5):
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
        k=k+2
    print()
