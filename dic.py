#  Dictionary for the characters and in-game items
characters = {
    "Pablo": {
        "Items:": "shiv, uniform, spoon",
        "Description:": "Arrested for gang violence, he is a good companion."
    },
    "Ricky": {
        "Items:": "police uniform, baton, money",
        "Description:": "Corrupt police officer, pay him for stuff."
    },
    "Jessica": {
        "Items:": "tape, uniform, shovel",
        "Description:": "Arrested for unknown reasons, she plans to dig out."
    },
    "Big Max": {
        "Items:": "police uniform, axe, baton",
        "Description:": "Police Captain, he is very un-forgiving"
    },
}

#  Dictionary for items
items = {
    "shovel": "tool used for digging",
    "uniform": "standard orange prison uniform",
    "police uniform": "uniform used by the police in game",
    "baton": "blunt weapon often used by police",
    "shiv": "a make-shift weapon, usually quite sharp",
    "spoon": "cutlery used for eating",
    "money": "can be used to buy stuff",
    "axe": "tool used for cutting trees, can be dangerous",
    "tape": "used to stick stuff together",
}


#  A function for characters used in main.py's menu screen
def char():
    """A proper character menu."""
    for characterN, characterI in characters.items():
        print(characterN)  # Prints characters in organized list


#  A function for items used in main.py's menu screen
def item_():
    """A proper item menu."""
    for IN, ID in items.items():
        print(IN.title())  # Prints items in organized list
