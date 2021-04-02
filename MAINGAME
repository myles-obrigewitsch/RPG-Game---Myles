#  Myles Obrigewitsch
#  CS 30
#  Period 1
#  2021/04/02
#  Nested dictionary RPG, containing inventory items, locations and characters

#  Dictionary for the characters, it is nested with a second dictionary
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
  "Big Papa": {
    "Items:": "police uniform, axe, baton",
    "Description:": "Police Captain, he is very un-forgiving"
  },
}

#  for loop that prints each character, desc., and items
for character, char_d in characters.items():
    for item1, item1d in char_d.items():
        print(f"{character}'s item/desc is, {item1} {item1d}")

#  Dictionary for inventory items, the top print statement makes a new line
print("")
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

#  for loop that prints each inventory item and it's description
for item, item_d in items.items():
    print(f"A {item.title()} is {item_d}.")  # This will print a statement

# Dictionary for locations, top top print statement is a new line
print("")
locations = {
  "prison cell": "a standard cell were prisoners are kept",
  "prison yard": "the outdoor yard for prisoners",
  "heavy duty cell": "a cell given to prisoners as punishment",
  "police office": "the police's office, prisoners not allowed here",
  "kitchen": "where food is made and given out",
}

#  for loop that prints each location and description
for location, location_d in locations.items():
    print(f"The {location.title()} is {location_d}.")  # Prints statement
