
print('''1=rock
2=paper
3=scissor''')
list={1:"rock",2:"paper",3:"scissor"}

p1=int(input("player 1 choose: "))
p2=int(input("player 2 choose: "))

#print("invalid")
#or (p2 > 3 or p2 <0):


if ( p1 <=0 or p1 >3 ) or (p2<=0 or p2 >3):
    print("invalid")
    

else:
    
    if list[p1]==list[p2]:
        print("draw")

    elif list[p1]=="rock" :
    
        if list[p2]=="paper":
            print(f"{p1} win  {list[p1]}")
        else :
           print(f"{p2} win {list[p2]}")

    elif  list[p1]=="paper" :
    
        if list[p2]=="scissor":
            print(f"{p2} win  {list[p2]}")
        else :
            print(f"{p1} win {list[p1]}")

    elif  list[p1]=="scissor" :
    
         if list[p2]=="rock":
            print(f"{p2} win  {list[p2]}")
         else :
           print(f"{p1} win {list[p1]}")


