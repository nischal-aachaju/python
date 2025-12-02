user_data="nischal"
password_data="Nischal1234!@$#"

user=input("Enter your user name : ")
password=input("Enter your password : ")

if user_data==user:
    if password_data==password:
        print("login succesfully")

    else:
        print("wrong password")
    

else:
    print("wrong user name")