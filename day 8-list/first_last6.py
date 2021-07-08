#first_last 6
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
a=[1,4,3,6]
if a[0]==6 or a[-1]==6 :
    print(True)
else:
    print(False)
