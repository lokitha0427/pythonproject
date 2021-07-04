#pattern 31
'''
A B C D E 
B C D E F 
C D E F G 
D E F G H 
E F G H I
'''
a=0
for i in range(0,5):
    for j in range(1,6):
        a=a+1
        print(chr(i+j+ord("@")),end=" ")
    print()
