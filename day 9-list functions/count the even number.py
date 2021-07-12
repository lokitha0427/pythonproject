#count the even numbers in the list
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
size=int(input())
x=[]
count=0
for i in range(size):
    x.append(int(input()))
for i in x:
    if i%2==0:
        count+=1
print(count)
