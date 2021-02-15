import os
path=r'c:\Users\向怀林\Desktop\new'
os.path.join("Users","向怀林","Desktop","new","neu.txt")
f=open("neu.txt","w")
f.write("Hi from Python!")
f.close()
my_list=list()
with open("neu.txt","r") as fu:
    my_list.append(fu.read())
print(my_list)

