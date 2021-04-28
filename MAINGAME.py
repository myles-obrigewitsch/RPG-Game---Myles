import dic
import locations
import characters
import player_name
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
            player_name.naming()  # Runs the next function
            break
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

#  Map function, more explained in function
def prison_map():
    """Creates map for the game using arrays"""
    map = [['', 'prison yard', ''],  # My grid map
           ['kitchen', 'cell', 'gym'],
           ['', 'guard room', '']]
    print("\n Here is a map of the prison:")
    print(tabulate(map, tablefmt='grid'))  # Uses tabulate package to print


#  While loop that provides the user with input
def start():
    """Function for all the actions"""
    prison_map()  # Prints our map before starting
    print("You can always type move in game to begin movement.")
    print("You awaken in prison yard, you cannot remember how you got here.")
    locations.prisonyard()  # Sends player to prison yard function

menu()  # Calls upon our menu to start the game
start()  # Runs the start of the game


