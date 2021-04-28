import characters

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

#  In seperate file to allow name used by everyone
