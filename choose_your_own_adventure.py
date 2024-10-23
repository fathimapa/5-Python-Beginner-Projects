name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("you are on a dirt road which comes to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'right':
    answer = input("You are near to a bridge, it huge , do you want to cross it or head back (cross , back) ? ").lower()

    if answer == "back":
        print("You go back and Lose!")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you want to talk to them (yes/no) ? ").lower()

        if answer == 'yes':
            print("you talk to the stranger and they give you gold. You WIN! ")
        elif answer == 'no':
            print("You ignored the stranger. You LOSE! ")
        else:
            print("Not a Valid option. You Lost! ")

    else:
        print("Not a valid option. You lost!")

elif answer == 'left':
    answer = input("You head to a river and also their is place to walk. do you want to (swim/walk) ? ").lower()

    if answer == 'walk':
        print("You walk miles and ran out of water and you Lost the game")
    elif answer == 'swim':
        print("you swim and you were eaten by a shark and You Lose! ")
    else:
        print("not a valid option . you Lose!")

else:
    print("Not a valid option , YOU LOSE! ")

print(f"Thank you for trying {name}")