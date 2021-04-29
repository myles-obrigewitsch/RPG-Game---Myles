#  Import statements
import locations
import menu_screen
from tabulate import tabulate


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


menu_screen.menu()  # Calls upon our menu to start the game
start()  # Calls upon start of game
