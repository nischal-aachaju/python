
#identity operator

name="ram"
name0="ram"
print(id(name))
print(id(name0))
print(name is name0) # true

list_name=["ram"]
list_name0=["ram"]
print(list_name is list_name0) # false , list is emutable

