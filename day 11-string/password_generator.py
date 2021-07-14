#create a password
first_name=input("enter your first name:")
last_name=input("enter your last name:")
mobile=input("enter your mobile number:")
print(f"Password is {first_name[:2]}{mobile[4:7]}{last_name[-2:]}")

