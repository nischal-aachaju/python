
a="nis@chal."

cleaner=a.maketrans({".":"r"," ":"","@":"","!":"","$":"","%":"","-":""})

password=a.translate(cleaner)
print(password)