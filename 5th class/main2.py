password=input("enter yout password: ").lower()
str1="aeiou"
str2="@3!0$"
word_tran=password.maketrans(str1,str2)

print(password.translate(word_tran) +"0##9")

