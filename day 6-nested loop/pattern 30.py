#pattern 30
'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
'''
a=0
for i in range(1,6):
    for j in range(1,6):
        a=a+1
        print(chr(a+ord("@")),end=" ")
    print()
