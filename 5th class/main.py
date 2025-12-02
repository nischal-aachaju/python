name=input("Enter your name : ")
user_name = name.lower()
list_name=user_name.split()

first_name = list_name[0]
last_name =list_name[1]

print(f"Hello {first_name}, Your full name is {first_name} {last_name}")


print("_".join(list_name))