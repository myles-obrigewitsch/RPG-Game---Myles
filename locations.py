import mapmovement
import characters
import player_name
import losingscreen

#  This creates a instance of a movement class
movement = mapmovement.Map("")

#  Global variables for quests
getspoon = False

#  Sets up input
option = ("What would you like to do?\n")

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
    global getspoon
    """Prison cell room function"""
    jessica = characters.Inmate("Jessica", "female",  # Instance of inmate class
    "prison clothes", "empty", "broken spoon")
    print("\nYou are in the cell room.")
    print("You notice an inmate hiding something.")
    print("(talk)(describe inmate)(inventory inmate)")
    while True:  # While loop for ingame options
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
            print(f"Jessica: Could you get me one {player_name.name}?(yes)(no)")
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


#  Function for the kitchen area
def kitchen():
    """Kitchen function"""
    print("\nYou are in the kitchen.")
    if getspoon == True:  # Activated if quest is accepted
        print("You see there is a spoon behind the counter.")
        print("Want to sneak and grab it, or take it and run?(sneak)(run)")
        while True:
            sneakorrun = input(option)
            if sneakorrun == "run":
                print("\nYou get caught by a guard, he tackles you.")
                print("You are sent to max security prison!")
                losingscreen.lose()  # Sends player to losing screen

    #  Will only run if getspoon is not accepted
    while getspoon == False:
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
    BigMax = characters.Captain("Big Max")
    Ricky = characters.Guard("Ricky")

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
