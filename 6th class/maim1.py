
# password=input("enter password: ")
password="nischal"
print("output".center(70))
first=password[0]
last=password[-1]
password_len=len(password)-2
print("*"*70)
# print(f"Your masked password: {first}{"*"*password_len}{last}".center(70))
print(f"Your masked password: {first}{"*"*password_len}{last}".center(70))
print("*"*70)