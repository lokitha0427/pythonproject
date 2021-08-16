#list comprehension
#values *2
a={"a":1,"b":2,"c":3}
b={k:v*2 for k,v in a.items()}
print(b)
