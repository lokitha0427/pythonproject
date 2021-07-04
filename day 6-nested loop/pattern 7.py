#pattern 7
'''
 1  3  5  7  9 
11 13 15 17 19 
21 23 25 27 29 
31 33 35 37 39 
41 43 45 47 49
'''
k=1
for i in range(5):
    for j in range(5):
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
        k=k+2
    print()
