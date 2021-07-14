#length of the password
password=input("Enter the password:")
if len(password)>=10:
    print("strong password")
elif len(password)>=5 and len(password)<=10:
    print("weak password")
else:
    print("poor password")
     
