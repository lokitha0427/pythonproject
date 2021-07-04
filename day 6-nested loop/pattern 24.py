#pattern 24
'''
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
'''
z=1
for i in range(1,6):
    for j in range(0,5):
        z=j%2
        print(z,end=" ")
    print()
