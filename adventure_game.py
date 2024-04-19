# In this code, I added a secret choice that allows players to 
# uncover a hidden passage with more than 2 options.

def main():
    print("You wake up in a dimly lit room. You see a DOOR and a WINDOW. What do you do?")
    choice = input(">> ").lower()

    if choice == "door":
        print("You open the door and find yourself in a hallway. There are two doors ahead labeled RED and BLUE. Which one do you choose?")
        inner_choice = input(">> ").lower()
        if inner_choice == "red":
            print("You enter the red room and find a treasure chest. Congratulations, you've found the treasure!")
        elif inner_choice == "blue":
            print("You enter the blue room and are met with a trap! You fall into a pit and lose the game.")
        else:
            print("Invalid choice. Please choose either RED or BLUE.")

    elif choice == "window":
        print("You approach the window and see a ladder outside. Do you CLIMB the ladder or STAY inside?")
        inner_choice = input(">> ").lower()
        if inner_choice == "climb":
            print("You climb out the window and escape to freedom!")
        elif inner_choice == "stay":
            print("You decide to stay inside, but the room begins to fill with poisonous gas. You lose the game.")
        else:
            print("Invalid choice. Please choose either CLIMB or STAY.")

    elif choice == "secret":
        print("You have uncovered a secret passage! You find yourself in a hidden chamber with three chests: GOLD, SILVER, and BRONZE. Which one do you open?")
        inner_choice = input(">> ").lower()
        if inner_choice == "gold":
            print("Congratulations! You've discovered the ultimate treasure and won the game!")
        elif inner_choice == "silver":
            print("You found a valuable item but it triggers a trap, and you lose the game.")
        elif inner_choice == "bronze":
            print("You found a small reward, but nothing extraordinary. You can keep playing or start over.")
        else:
            print("Invalid choice. Please choose either GOLD, SILVER, or BRONZE.")

    else:
        print("Invalid choice. Please choose either DOOR, WINDOW, or SECRET.")

if __name__ == "__main__":
    main()
