import characters
import losingscreen
import locations
from tabulate import tabulate

# Introducing global variable
name = ""


#  Player naming function, using player class
def naming():
    """Allows player to select their name"""
    global name  # Uses the global variable I set up
    name_start = ("Tell us your players name:\n")
    name = input(name_start)
    main_player = characters.Player(name)
    main_player.say_name()  # Says name back to player
    
    if losingscreen.LOST == True:
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

        start()

#  In seperate file to allow name used by everyone
