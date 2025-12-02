print("welcome to the game ")
direction = input("do you want to go north or south ")

if direction == "south":
    print("game over ")
    print("choose next path")

elif direction == "north":
    dir_north=input("cross the river or follow the path ")

    if dir_north == "cross":
        print("game over")
        print("choose next path")
    elif dir_north == "follow the path":

        dir_follow_path=input("fairy or ogre ot elf ")

        if dir_follow_path == "fairy" or dir_follow_path == "ogre":

            print("gamr over")
            print("choose next path")

        elif dir_follow_path == "elf":

            print("you win")

        else:
            print("invalid input")

    else:
        print("invalid input")

else:
    print("invalid input")
