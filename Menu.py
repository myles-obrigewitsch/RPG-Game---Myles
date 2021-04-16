#  Starting text for game, this code is used in the while loop
main_menu = ("Welcome to PRISON ESCAPE!\n")
main_menu += ("Type play to enter game, or quit to end game.\n")


#  Function / while loop that runs a menu function
def menu():
    """Menu screen function, can be easily accessed"""
    while True:
        menu_action = input(main_menu)
        if menu_action == "play":
            print("")
            flag()  # Runs the next function
        elif menu_action == "quit":
            print("\nLeaving game...\n")
            break  # Ends the game
        else:
            print("\nInvalid Action\n")  # Runs if there is not a valid input

#  Sets up the actions
starting = ("You awaken in a prison yard, would you like to:")
starting += ("\nGo to your cell?(cell)")
starting += ("\nGo to the kitchen?(kitchen)")
starting += ("\nTalk to an inmate?(inmate)")
starting += ("\nDig a hole in the yard??(dig)")
starting += ("\n(Type quit to head back to menu.)")


#  While loop that provides the user with input
def flag():
    """Function for all the actions"""
    while True:
        action = input(starting)  # Where we get player input
        if action == "cell":
            print("\nYou go to your cell.\n")
        elif action == "kitchen":
            print("\nYou go the kitchen.\n")
        elif action == "inmate":
            print("You try to talk to the inmate but he shanks you...")
            print("\nYou died!\n")
            break
            menu()
        elif action == "dig":
            print("\nThe guards catch you digging in the open.")
            print("You get sent to maximum security.\n")
        elif action == "quit":
            print("\nGoing back to main menu!\n")
            break
            menu()  # Brings the player back to the menu
        else:
            print("\nInvalid action, try again.\n")

menu()  # Calls upon our menu to start the game
