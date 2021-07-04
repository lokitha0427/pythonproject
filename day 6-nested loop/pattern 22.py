#pattern 22
'''
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0
'''
k=1
for i in range(0,5):
    for j in range(1,6):
        k=i%2
        print(k,end=" ")
    print()
