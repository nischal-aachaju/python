
ATM = True
amt=5000
pin=123
if ATM:
    pin_code=int(input("enter pin code : "))
    if pin==pin_code:
        print("""
1. withdraw
2. Check Balance
3. Exit          
""")
        chooes=int(input("enter number to choose : "))
        if chooes==2:
            print(f"Your Balance = {amt}")   
        elif chooes==3:
            print("Exit")
        elif chooes ==1:
            print("withdraw amount")
            withdraw_atm=int(input("enter amount : "))
            if withdraw_atm<500:
                print("should be greter then 500")
            elif withdraw_atm <= amt:
                print("Get the cash")
                print(f"Remaining amount= {amt-withdraw_atm} ")
            else :
                  print("not enough money")
    else:
        print("invalid pin")
else:
    print("ATM expire or invalid")
print("Thanks for visiting".center(40,"*"))



