# q1   positive negative 
# num= int(input("enter number: "))

# if (num > 0):
#     print(f"{num} is Positive ")

# elif (num < 0):
#     print(f"{num} is Negative")

# else:
#     print(f"Zero")


#q2 range bth 1 to 100
# num= int(input("Number? "))

# if (num >=1 and num <= 100):
#     print(f"{num} is in between 1 to 100")

# else:
#     print(f"{num} is not in between 1 to 100 ")

#q3 odd even

# num= int(input("enter numnber"))

# if (num ==0):
#     print("The number is Zero")
# elif (num %2==0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

#q4 grade system

# mark=int(input("enter marks "))
# if (mark >100 or mark <0):
#     print("Invalid mark")
# elif (mark <= 100 and mark >90):
#     print(f"{mark } is A+")

# elif (mark <=90 and mark >80):
#     print(f"{mark} is A")

# elif (mark <=80 and mark >70):
#     print(f"{mark} is B+")

# elif (mark <=70 and mark > 60):
#     print(f"{mark} is B+")

# elif (mark <=60 and mark >50):
#     print(f"{mark} is B")

# else:
#     print("fail")


#q5 basic calculator

first_num=int(input("enter 1st number : "))
second_num=int(input("enter 2nd number : "))
op= input("ener operatior :(+ , - , * ,/) ")

if "+" in op:
    print(f'{first_num+second_num} ')

elif "-" in op:
    print(f'{first_num-second_num} ')
elif "*" in op:
    print(f'{first_num*second_num} ')
elif "/" in op:
    if second_num==0:
        print("Invalid number")
    else:
        print(f'{first_num/second_num}')

else:
    print("Invalid operator")
