#pattern 29
'''
E D C B A 
E D C B A 
E D C B A 
E D C B A 
E D C B A
'''
for i in range(5):
    for j in range(ord('E'),ord('@'),-1):
        print(chr(j),end=" ")
    print()
