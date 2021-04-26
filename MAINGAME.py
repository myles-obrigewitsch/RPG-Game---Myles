import dic
import classes
from tabulate import tabulate


#  Map class used for movement, has to be in this file for the time being
class Map:
    """Basic map class"""

    def __init__(self, test):
        """Init statement"""
        self.test = test

    #  Each attribute from here will allow player to move in game
    def prison_yard(self):
        """Sets up movement in the prison yard"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "south":
                cell()
                break
            else:
                print("You cannot go that way.")

    def cell(self):
        """Sets up movement in the cell"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "south":
                guard_enc()
                break
            elif self.direction == "north":
                print("")  # Used to create an in game indent (MAYBE CHANGE)
                prisonyard()
                break
            elif self.direction == "east":
                gym()
                break
            elif self.direction == "west":
                kitchen()
                break
            else:
                print("You cannot go that way.")

    def kitchen(self):
        """Sets up movement in the kitchen"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "east":
                cell()
                break
            else:
                print("You cannot go that way.")

    def gym(self):
        """Sets up movement in the gym"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "west":
                cell()
                break
            else:
                print("You cannot go that way.")

    def guard_room(self):
        """Sets up movement in the guard room"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "north":
                cell()
                break
            else:
                print("You cannot go that way.")

#  This creates a instance of a movement class
movement = Map("")

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
            naming()  # Runs the next function
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


#  Player naming frunction, using player class
def naming():
    """Allows player to select their name"""
    name_start = ("Tell us your players name:\n")
    name = input(name_start)

    main_player = classes.Player(name)
    main_player.say_name()
    flag()  # Runs the start of the game


#  Map function, more explained in function
def prison_map():
    """Creates map for the game using arrays"""
    map = [['', 'prison yard', ''],  # My grid map
           ['kitchen', 'cell', 'gym'],
           ['', 'guard room', '']]
    print("\n Here is a map of the prison:")
    print(tabulate(map, tablefmt='grid'))  # Uses tabulate package to print


#  Sets up input
option = ("What would you like to do?\n")


#  While loop that provides the user with input
def flag():
    """Function for all the actions"""
    prison_map()  # Prints our map before starting
    print("You can always type move in game to begin movement.")
    print("You awaken in prison yard, you cannot remember how you got here.")
    prisonyard()  # Sends player to prison yard function


#  Function for the prison yard area
def prisonyard():
    """Prison yard function"""
    print("The prison yard is grey, and lonely.")
    while True:
        decide = input(option)
        if decide == "move":
            movement.prison_yard()  # Goes to movement class
            break
        else:
            print("Invalid action, try again.\n")


#  Function for the cell area
def cell():
    """Prison cell room function"""
    print("\nYou are in the cell room.")
    while True:
        decide = input(option)
        if decide == "move":
            movement.cell()
            break
        else:
            print("Invalid action, try again.\n")


#  Function for the kitchen area
def kitchen():
    """Kitchen function"""
    print("\nYou are in the kitchen.")
    while True:
        decide = input(option)
        if decide == "move":
            movement.kitchen()
            break
        else:
            print("Invalid action, try again.")


#  Function for the gym area
def gym():
    """Gym function"""
    print("\nYou are in the gym.")
    while True:
        decide = input(option)
        if decide == "move":
            movement.gym()
            break
        else:
            print("Invalid action, try again.")


#  Guard room
def guard_enc():
    """Guard encounter"""
    BigMax = classes.Captain("Big Max")
    Ricky = classes.Guard("Ricky")

    encounter = ("\nIn the guard room you see a captain and regular guard.")
    encounter += ("\nType describe captain or describe guard for description.")
    encounter += ("\nType status captain or status guard to check status.\n")
    #  While loop that will allow for repeating actions
    while True:
        response = input(encounter)
        if response == "describe captain":
            print("")
            BigMax.describe_g()
        elif response == "describe guard":
            print("")
            Ricky.describe_g()
        elif response == "status captain":
            print("")
            BigMax.status()
        elif response == "status guard":
            print("")
            Ricky.status()
        elif response == "move":
            movement.guard_room()
            break
        else:
            print("\nInvalid action, try again.\n")

menu()  # Calls upon our menu to start the game
