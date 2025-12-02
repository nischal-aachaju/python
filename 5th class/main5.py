

email=input("Enter your email : ").lower()
unclean_username= email.replace("@gmail.com","")

cleaner=unclean_username.maketrans({".":""," ":"","@":"","!":"","$":"","%":"","#":""})

clean_username=unclean_username.translate(cleaner)
print(f"User Name : {clean_username}")

