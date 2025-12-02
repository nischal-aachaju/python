#         practice_questions.pdf   

# 1) Take a number and print “Even” or “Odd”. 
# number = int(input(" enter number"))

# if number ==0:
#     print("the number is zero")

# elif number %2==0:
#     print(f"{number} is even")

# else :
#     print(f"{number} is odd")

# 2) Take a character and print “Vowel” or “Consonant”.  it is hard code so it take number as consonant

# word= input("enter character : ")

# char=word[0].lower()

# if char == "a" or char =="e" or char =="i" or char =="o" or char=="u":
#     print(f"{char} is vowel")

# else :
#     print("consonant")

# 3) Take age and print “Minor” if <18, else “Adult”

# age =int(input("enter age : "))

# if age<18:
#     print("Minor")

# else:
#     print("Adult")

#4 ) Take marks (0–100) and print “Pass” if ≥40, else “Fail”

# mark= int (input("enter marks "))

# if mark>=40 and mark <=100:
#     print("pass")

# elif mark <40:
#     print("fail")

# else:print("invalid marks")

#5 ) Take 3 numbers and print the largest using only if-else

# num1=int(input("enter 1st num "))
# num2=int(input("enter 2nd num "))
# num3=int(input("enter 3rd num "))

# if num1>= num2:
#     if num1>= num3:
#         print(f"{num1} is largest")
#     else:
#         print(f"{num3} is largest")

# elif num2>= num3:
#     if num2>= num1:
#         print(f"{num2} is largest")
#     else:
#         print(f"{num1} is largest")

# elif num3>=num1:
#     if num3>= num2:
#         print(f"{num3} is largest")
#     else:
#         print(f"{num2} is largest")

# else:
#     print("invalid number")

#6 Take a month number (1–12) and print the month name.

# month=int(input("enter the number of month : "))

# list ={1:"January",2:"February" ,3:"March" ,4:"April" , 5:"May" ,6:"June" ,7:"July" , 8:"August" ,9:"September" ,10:"October" ,11:"November ", 12:"December"} 

# print(list[month])

#7 )Take temperature in Celsius → print “Hot” (>35), “Warm” (25–35),“Cold” (<25). 

# temp = int(input("enter temperature : "))

# if temp> 35:
#     print("HOT")

# elif temp <=35 and temp >=25:
#     print("warm")

# elif temp <25 :
#     print("cold")

# else :
#     print("invalid temperature")

#8 ) Take salary → if >50000 print “High”, elif >30000 print “Medium”,else “Low”. 

# sal = int(input("enter salary : "))

# if sal> 50000:
#     print("High")



# elif sal >30000 :
#     print("Mediun")

# else :
#     print("Low")


#9 Take a number → print “Positive”, “Negative”, or “Zero”.

# num= int (input("enter number"))

# if num==0:
#     print("zero")

# elif num >0:
#     print("positive")

# elif num< 0:
#     print("Negative")


#10) Take day number (1–7) → print “Weekday” or “Weekend”

# day =int(input("enter day "))

# if day <6 and day >0:
#     print("Weekday")

# elif day==7:
#     print("weekend")

# else :
#     print("invalid data")

#11) Take a number → check if it is divisible by both 5 and 7.

# num=int(input("enter number : "))

# if num %5 ==0 and num %7 ==0:
#     print(f"{num} is divisible by both 5 and 7")

# else :
#     print(f" {num } is not divisible by both 5 and 7 ")


#12 range bth 1 to 100
# num= int(input("Number? "))

# if (num >=1 and num <= 100):
#     print(f"{num} is in between 1 to 100")

# else:
#     print(f"{num} is not in between 1 to 100 ")

#13 grade system 

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


# 14 basic calculator

# first_num=int(input("enter 1st number : "))
# second_num=int(input("enter 2nd number : "))
# op= input("ener operatior :(+ , - , * ,/) ")

# if "+" in op:
#     print(f'{first_num+second_num} ')

# elif "-" in op:
#     print(f'{first_num-second_num} ')
# elif "*" in op:
#     print(f'{first_num*second_num} ')
# elif "/" in op:
#     if second_num==0:
#         print("Invalid number")
#     else:
#         print(f'{first_num/second_num}')

# else:
#     print("Invalid operator")


#15 bonus calculator

# sal=int(input("enter your sallery : "))
# yrs=int(input("enter your experiences: "))

# if yrs> 10:
#     print("bonus=10%")
#     bon=sal*0.1
#     total=sal+sal*0.1
   

# elif yrs >=6 and yrs <=10:
#     print("bonus=8%")
#     bon=sal*0.08
#     total=sal+sal*0.08
    
    
# else :
#     print("bonus=5%")
#     bon=sal*0.05
#     total=sal+sal*0.05
    

# print(f"bonus={bon}")
# print(f"total={total}")


#16 qustion game ot choose Welcome to the Magic Fores

# print("welcome to the spece mission")
# user=input("choose : to the moon or to mars ")

# if user=="to mars":
#     print("game over")

# elif user=="to the moon":
#     print("okey")

#     user=input("choose: land on the surface or stay in orbit ")

#     if user =="land on the surface":
#         print("game over")
#     elif user=="stay in orbit":
#         print("okey")
#         user=input("choose:alien or asteroid or satellite ")

#         if user=="alien" or user=="asteroid":
#             print("game over")
#         elif user =="satellite":
#             print("you win")

#         else:
#             print("invalid input")

#     else:
#         print("invalid input")
# else:
#         print("invalid input")

#17 (wages acc to age and gender)
# age=int(input("enter age "))
# gen=input("enter gender (M OR F) ")

# if age >=18 and age <30:
#     if gen=="M":
#         print(f"Gender= {gen}")
#         print("wage/day = 700")
#     elif gen =="F":
#         print(f"Gender= {gen}")
#         print("wage/day = 750")
#     else:
#         print("invalid")

    

# elif (age >=30 and age<=40):
#     if gen=="M":
#         print(f"Gender= {gen}")
#         print("wage/day = 800")
#     elif gen =="F":
#         print(f"Gender= {gen}")
#         print("wage/day = 850")
#     else:
#         print("invalid")

# else:
#     print("invalid age")

#18   Welcome to the Magic Fores
# print("welcome to the game ")
# direction = input("do you want to go north or south ")

# if direction == "south":
#     print("game over ")
#     print("choose next path")

# elif direction == "north":
#     dir_north=input("cross the river or follow the path ")

#     if dir_north == "cross":
#         print("game over")
#         print("choose next path")
#     elif dir_north == "follow the path":

#         dir_follow_path=input("fairy or ogre ot elf ")

#         if dir_follow_path == "fairy" or dir_follow_path == "ogre":

#             print("gamr over")
#             print("choose next path")

#         elif dir_follow_path == "elf":

#             print("you win")

#         else:
#             print("invalid input")

#     else:
#         print("invalid input")

# else:
#     print("invalid input")
