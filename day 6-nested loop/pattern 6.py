'''
 1  2  3  4  5 
 6  7  8  9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
'''
k=1
for i in range(5):
    for j in range(5):
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
        k=k+1
    print()
    
