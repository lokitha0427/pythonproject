#pattern 25
'''
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1 
1 0 1 0 1
'''
z=1
for i in range(0,5):
    for j in range(1,6):
        z=j%2
        print(z,end=" ")
    print()
