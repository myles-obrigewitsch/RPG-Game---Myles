#  Myles Obrigewitsch
#  CS 30
#  Period 1
#  2021/04/19
#  A RPG map and imported character modules, organized in game style

#  Imports all info from dic.py and tabulate package
import dic
from tabulate import tabulate

#  Starting text for game, this code is used in the while loop
main_menu = ("Welcome to PRISON ESCAPE!\n")
main_menu += ("Type play to enter game, or quit to end game.\n")
main_menu += ("To show characters type characters.\n")
main_menu += ("To show items type items.\n")


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
        elif menu_action == "characters":
            print("\nCharacters in game:")
            dic.char()
            print("")  # Prints all characters
        elif menu_action == "items":
            print("\nItems in game:")
            dic.item_()
            print("")  # Prints all items
        else:
            print("\nInvalid Action\n")  # Runs if there is not a valid input


#  Sets up the actions
starting = ("You awaken in the prison yard, would you like to:")
starting += ("\nGo to your cell?(cell)")
starting += ("\nGo to the kitchen?(kitchen)")
starting += ("\nGo to the guard room?(guard room)")
starting += ("\nGo to the gym? (gym)")
starting += ("\nFor future refrence, prison yard = yard.")
starting += ("\n(Type quit to head back to menu.)")

#  Allows for input after starting game
test = ""


#  Map function, more explained in function
def prison_map():
    """Creates map for the game using arrays"""
    map = [['', 'prison yard', ''],  # My grid map
           ['kitchen', 'cell', 'gym'],
           ['', 'guard room', '']]
    print("\n Here is a map of the prison:")
    print(tabulate(map, tablefmt='grid'))  # Uses tabulate package to print


#  While loop that provides the user with input
def flag():
    """Function for all the actions"""
    prison_map()  # Prints our map before starting
    print(starting)
    while True:
        action = input(test)  # Where we get player input
        if action == "cell":  # These series of elif statements let you move
            print("\nYou go to your cell.")
            print("Where would you like to go now?\n")
        elif action == "kitchen":
            print("\nYou go to the kitchen.")
            print("Where would you like to go now?\n")
        elif action == "guard room":
            print("\nYou go to the guard room.")
            print("Where would you like to go now?\n")
        elif action == "gym":
            print("\nYou go to the gym.")
            print("Where would you like to go now?\n")
        elif action == "yard":
            print("\nYou go to the prison yard.")
            print("Where would you like to go now?\n")
        elif action == "quit":
            print("\nGoing back to main menu!\n")
            break
            menu()  # Brings the player back to the menu
        else:
            print("\nInvalid action, try again.\n")

menu()  # Calls upon our menu to start the game
