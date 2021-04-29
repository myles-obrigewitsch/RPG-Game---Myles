#  Import statements
import map_movement
import characters
import player_name
import losing_screen
import win_or_lose

#  This creates a instance of a movement class
movement = map_movement.Map("")

#  Global variables for quests
getspoon = False
firstchance = False
haveshovel = False
haveknife = False
havemoney = False

#  Sets up input
option = ("What would you like to do?\n")


#  Function for the prison yard area
def prisonyard():
    """Prison yard function"""
    global haveknife  # Sets up global have knife variable
    print("\nThe prison yard is grey, and lonely.")
    print("The only thing in the courtyard is a big rock.(rock)")
    while True:
        decide = input(option)
        if decide == "move":
            movement.prison_yard()  # Goes to movement class
            break
        elif decide == "rock":
            if haveshovel is False:
                print("\nYou go the rock and see a knife lodged under it.")
                print("You could get it if you had a shovel...")
            elif haveshovel is True:
                print("\nYou dig up the knife, and take it with you!")
                print("New Objective: Get money from buff inmate.")
                haveknife = True  # sets global value to true
        else:
            print("Invalid action, try again.\n")


#  Function for the cell area
def cell():
    global getspoon
    global firstchance
    """Prison cell room function"""
    jessica = characters.Inmate("Jessica", "female",  # Inmate class instance
                                "prison uniform", "empty", "broken spoon")

    print("\nYou are in the cell room.")
    print("You notice an inmate hiding something.")
    print("(talk)(describe inmate)(inventory inmate)")
    while firstchance is False:  # While loop for ingame options
        decide = input(option)
        if decide == "move":
            movement.cell()
            break
        elif decide == "describe inmate":
            print("")
            jessica.describe_I()
        elif decide == "inventory inmate":
            print("")
            jessica.inventory()
        elif decide == "talk":  # This will allow player to interact to Jessica
            print("\nJessica: I am almost done digging this hole!")
            print("Jessica: I need a new spoon from the kitchen.")
            print(f"Jessica: Could you get it {player_name.name}?(yes)(no)")
            while True:  # New while loop for yes or no decision
                yesorno = input(option)
                if yesorno == "yes":
                    print("\nJessica: Perfect thanks!")
                    print("New objective: Get Jessica a spoon.")
                    getspoon = True  # This starts the getspoon quest
                    break
                elif yesorno == "no":
                    print("\nJessica: Fine, rot in prison then!")
                    break
                else:
                    print("Invalid action, try again.\n")
        else:
            print("Invalid action, try again.\n")


#  If you made it far enough in quest this will run
    while firstchance is True:  # Global variable
        win_or_lose.morales()
        firstchance = False


#  Function for the kitchen area
def kitchen():
    """Kitchen function"""
    print("\nYou are in the kitchen.")
    global firstchance
    if getspoon is True:  # Activated if quest is accepted
        print("You see there is a spoon behind the counter.")
        print("Want to sneak and grab it, or take it and run?(sneak)(run)")
        while True:
            sneakorrun = input(option)
            if sneakorrun == "run":
                print("\nYou get caught by a guard, he tackles you.")
                print("You are sent to max security prison!")
                losing_screen.lose()  # Sends player to losing screen
            if sneakorrun == "sneak":
                print("\nYou go by unnoticed, the spoon is now yours!")
                print("New objective: Bring spoon back to Jessica.")
                firstchance = True  # sets global value true
                decide = input(option)
                if decide == "move":
                    movement.kitchen()
                    break
                else:
                    print("Invalid action, try again.\n")
                break

    #  Will only run if getspoon is not accepted
    while getspoon is False:
        decide = input(option)
        if decide == "move":
            movement.kitchen()
            break
        else:
            print("Invalid action, try again.\n")


#  Function for the gym area
def gym():
    """Gym function"""
    global haveshovel  # Uses global variables
    global haveknife
    global havemoney
    pablo = characters.Inmate("Pablo", "Male",
                              "prison uniform", "pure muscles", "empty")

    print("\nYou are in the gym.")
    print("You see there is a buff guy protecting money.")
    print("You see a shovel being used as a dumbell.")
    print("(fight)(describe enemy)(inventory enemy)(take shovel)")
    while True:
        decide = input(option)
        if decide == "move":
            movement.gym()
            break
        elif decide == "take shovel":  # Picks up shovel
            print("\nYou picked up the shovel.")
            print("New Objective: Dig up knife in prison yard.")
            haveshovel = True
        elif decide == "describe enemy":  # Calls upon inmate instance
            print("")
            pablo.describe_I()
        elif decide == "inventory enemy":
            print("")
            pablo.inventory()
        elif decide == "fight":  # Sets up fight, player loses without knife
            if haveknife is False:
                print("\nYou go to fight him but he smacks you hard.")
                print("Your life slowly fades away...")
                losing_screen.lose()
                break
            elif haveknife is True:
                print("\nHe sees your knife and begins to cry.")
                print("He gives you the money he was protecting.")
                print("New Objective: Bribe Guards.")
                havemoney = True  # sets money variable to true
        else:
            print("Invalid action, try again.\n")


#  Guard room
def guard_enc():
    """Guard encounter"""
    global havemoney
    ricky = characters.Guard("Ricky")  # Sets up guard instance

    print("\nYou are in the guard room")
    print("You see the corrupt guard Ricky is there.")
    print("(describe guard)(bribe)")
    while True:
        response = input(option)
        if response == "describe guard":
            print("")
            ricky.describe_g()
        elif response == "bribe":
            if havemoney is False:  # variable to detect if you have money
                print("\nRicky: You do not have any money idiot!")
            if havemoney is True:
                print("\nYou hand him the buff mans money.")
                print(f"Ricky: This will suffice {player_name.name}.")
                print("He escorts you out of prison quietly...")
                print("YOU WIN!")
                break
        elif response == "move":
            movement.guard_room()
            break
        else:
            print("Invalid action, try again.\n")
