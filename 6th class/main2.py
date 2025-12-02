
input="nischal"
re=input.maketrans({"a":"✈️","e":"🐘","i":\
                    "🍦","o":"🍊","u":"☂️"})
tran=input.translate(re)
print("input"+"output".rjust(32)) 
print(input +"Secret Code :aeiou".rjust(44))
print(f"Emoji Code:{tran}".rjust(49)) 