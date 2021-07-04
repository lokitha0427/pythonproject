#pattern 20
'''
1 0 1 0 1 
0 0 0 0 0 
1 0 1 0 1 
0 0 0 0 0 
1 0 1 0 1 
'''
k=1
for i in range(1,6):
    for j in range(1,6):
        k=(i*j)%2
        print(k,end=" ")
    print()
