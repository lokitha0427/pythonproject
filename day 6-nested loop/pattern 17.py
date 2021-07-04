#pattern 17
'''
 1  3  5  7  9 
 3  5  7  9 11 
 5  7  9 11 13 
 7  9 11 13 15 
 9 11 13 15 17
 '''
k=1
for i in range(1,6):
    for j in range(1,6):
        k=2*(i+j)-3
        if k<10:
            print(" "+str(k),end=" ")
        else:
            print(k,end=" ")
    print()
