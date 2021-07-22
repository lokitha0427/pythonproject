#string into dictionary
str="name=loki age=23 place=pondy"
dict={}
for i in str.split(" "):
    k,v=i.split("=")
    dict[k]=v
print(dict)
