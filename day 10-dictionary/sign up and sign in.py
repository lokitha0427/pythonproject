#sign up and sign in
user={}
while True:
    ch=int(input("1.sign up 2.sign In 3.exit"))
    if ch==1:
        uname=input("Username:")
        email=input("Email")
        mobile=input("Mobile")
        password=input("Password")
        if uname in user:
            print("user name is already exist")
        else:
            user.setdefault(uname,[email,mobile,password])
            print("Account is created successfully")
    elif ch==2:
        uname=input("Username")
        password=input("Password")
        if(((uname in user) or uname in user[uname][0]) and (password in user[uname][2])):
            print("login is success")
        else:
            print("unauthorised user")
    else:
        break
