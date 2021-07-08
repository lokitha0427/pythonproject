#sum2
#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
a=[1,2,3]
if len(a)>2:
    print(a[0]+a[1])
else:
    print(0)

