
u_password=input("enter password: ")
print("output".center(70))
cleaner=u_password.maketrans({".":""," ":"","@":"","!":"","$":"","%":"","-":""})

password=u_password.translate(cleaner)
first=password[0:4]
last=password[9:14:1]
password_len=len(password)-7
print("*"*70)
print(password.center(70))
print(f"Your masked password: {first}{"*"*password_len}{last}".center(70))

print("*"*70)







