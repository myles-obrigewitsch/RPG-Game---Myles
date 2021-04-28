import player_name
import sys
import os

#  Function found from internet, used to restart program
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


#  Called when player loses the game
def lose():
    """Function for losing screen"""
    dead = (f"\nSorry {player_name.name}, you lost!")
    dead += ("\nWould you like to try again?\n")
    while True:
        choice999 = input(dead)
        if choice999 == "yes":
            print("Restarting game...\n")
            restart_program()  # Calls upon game to restart
            break
        elif choice999 == "no":
            print("\nEnding game...")
            break
        else:
            print("Invalid action, try again.\n")