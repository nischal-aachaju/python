
wet=float(input("enter the weight : "))
print("""
1= Mercury
2= Venus
3= Mars
4= Jupiter
5= Saturn
6= Uranus
7= Neptune
""")
pla=int(input("choose planet : "))

if pla <0 or pla >7:
    print("invalid choose")

list_pla={ 1: "Mercury",
2: "Venus",
3: "Mars",
4: "Jupiter",
5: "Saturn",
6: "Uranus",
7: "Neptune" }

print (f"you choose : {list_pla[pla]}")
list_rg={ 1: 0.38,
2: 0.91,
3: 0.38,
4: 2.53,
5: 1.07,
6: 0.89,
7: 1.14 }

user_wt=wet*list_rg[pla]
print(f"{user_wt}kg in {list_pla[pla]} ")
