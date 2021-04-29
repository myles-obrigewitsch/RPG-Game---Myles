#  Import statements
import player_name
import losing_screen


#  Sets up input
option = ("What would you like to do?\n")


#  Players chance to win or lose game
def morales():
    """Scenario function"""
    loop = True  # sets up game to end
    if loop is True:
        print("\nYou return to the cell room.")
        print("You see the police captain, Big Max, scouting out the cell.")
        print("Big Max walks up to you.")
        print(f"Big Max: {player_name.name} do you know what's going on here?")
        print("\nChoice 1: Sell out Jessica. (sell out)")
        print("\nChoice 2: Take the blame for the hole. (sacrifice)\n")
        while True:
            bigchoice = input(option)
            if bigchoice == "sell out":
                print("\nJessica is caught, she looks ashamed of you...")
                print("Big Max releases you due to good behaviour!")
                print("YOU WIN!")  # Player wins game
                loop = False
                break
            elif bigchoice == "sacrifice":
                print("You take the blame, but Jessica manages to escape.")
                print("You are sent to Max security prison...")
                losing_screen.lose()  # Sends player to losing screen
                break
            else:
                print("Invalid action, try again.\n")
