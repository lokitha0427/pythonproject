#simple interest function
def si(r=1.5):
    p=(int(input("Enter the principle:")))
    n=(int(input("Enter the number of years:")))
    print((p*n*r)/100)
si()
