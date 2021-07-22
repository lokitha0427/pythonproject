#nested list
a=[[1,[jaya,21,pondy]],[2,[vijay,22,chennai]],[3,[tamizh,23,salem]]]
while True:
    n=int(input("Enter the number:"))
    if n in a:
        print("name:",a[n][0])
        print("age:",a[n][1])
        print("palce:",a[n][2])
    else:
        print("invalid number")
