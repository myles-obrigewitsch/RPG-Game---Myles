import mapmovement
import characters

#  This creates a instance of a movement class
movement = mapmovement.Map("")

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
    """Prison cell room function"""
    jessica = characters.Inmate("Jessica", "Female",
        "prison clothes", "none", "broken spoon")
    print("\nYou are in the cell room.")
    print("You notice an inmate hiding something.")
    print("(talk)(describe inmate)(inventory inmate)")
    while True:
        decide = input(option)
        if decide == "move":
            movement.cell()
            break
        elif decide == "describe inmate":
            print("")
            print(jessica.describe_I())
        elif decide == "inventory inmate":
            print("")
            print(jessica.inventory())
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
