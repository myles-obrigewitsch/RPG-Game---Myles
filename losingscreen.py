import player_name
import menuscreen


# Sets up global variable
LOST = False

#  Called when player loses the game
def lose():
    """Function for losing screen"""
    global LOST
    dead = (f"\nSorry {player_name.name}, you lost!")
    dead += ("\nWould you like to return to menu?\n")
    while True:
        choice999 = input(dead)
        if choice999 == "yes":
            print("\nTalking you back to menu...\n")
            LOST = True
            menuscreen.menu()
            break
        elif choice999 == "no":
            print("\nEnding game...")
            break
        else:
            print("\nInvalid input, try again.")