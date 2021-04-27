import locations

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
                locations.cell()
                break
            else:
                print("You cannot go that way.")

    def cell(self):
        """Sets up movement in the cell"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "south":
                locations.guard_enc()
                break
            elif self.direction == "north":
                print("")  # Used to create an in game indent (MAYBE CHANGE)
                locations.prisonyard()
                break
            elif self.direction == "east":
                locations.gym()
                break
            elif self.direction == "west":
                locations.kitchen()
                break
            else:
                print("You cannot go that way.")

    def kitchen(self):
        """Sets up movement in the kitchen"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "east":
                locations.cell()
                break
            else:
                print("You cannot go that way.")

    def gym(self):
        """Sets up movement in the gym"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "west":
                locations.cell()
                break
            else:
                print("You cannot go that way.")

    def guard_room(self):
        """Sets up movement in the guard room"""
        print("\nWhat direction do you want to go?")
        while True:
            self.direction = input(self.test)
            if self.direction == "north":
                locations.cell()
                break
            else:
                print("You cannot go that way.")
