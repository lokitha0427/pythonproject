#sign in sign up
while True:
    ch=int(input("choice:"))
    if ch==1:
        r=open("test.txt","r")
        w=open("test.txt","a")
        uname=input("username:")
        password = input("password:")
        mobile = input("mobile:")
        for i in r:
            if uname in i:
                print("username is already exist")
                break
        else:
            w.write(uname+"/t"+password+"/t"+mobile+"/n")
            print("Account is created successfully")
            w.close()
            r.close()
    elif ch==2:
        r=open("test.txt","r")
        uname = input("username:")
        password = input("password:")
        for i in r:
            if uname in i and password in i:
                print("login is success")
        else:
            print("unauthorized user")
            r.close()
    else:
        break