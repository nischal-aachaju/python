#In a smart building lift system, the lift is currently at floor 5.
# A person pressesfloor 3. Write a program to decide and display 
# whether the lift should go up, godown, or stay at current floor.

lift =5
btn_press=3
if lift > btn_press:
    print(f"Lift go down and stop at {btn_press}")

elif lift < btn_press:
    print(f"Lift go up and stop at {btn_press}")

elif lift == btn_press:
    print("lift stay at current floor")

else :
    print("error")

