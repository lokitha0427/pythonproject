#pattern 28
'''
E E E E E 
D D D D D 
C C C C C 
B B B B B 
A A A A A 
'''
for i in range(ord('E'),ord('@'),-1):
    for j in range(5):
        print(chr(i),end=" ")
    print()
