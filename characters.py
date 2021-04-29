#  This is a file for classes, these include character classes so far


#  Player class
class Player:
    """A class to describe player"""

    def __init__(self, name):
        """The init statement"""
        self.name = name

    def say_name(self):
        """Will print players name"""
        print(f"Your players name is {self.name.upper()}.")


#  Guard class
class Guard:
    """A class modelling a guard"""

    def __init__(self, gname):
        """Init statement"""
        self.gname = gname

    def describe_g(self):
        """Describes guard"""
        print(f"They wear a gold badge, thier name is {self.gname}.")

    def status(self):
        """Shows the status of a guard"""
        print("This is a level 1 guard.")


#  Subclass of guard
class Captain(Guard):
    """Class modelling a guard captain"""

    def __init__(self, gname):
        """Init statement"""
        super().__init__(gname)

    def status(self):
        """Shows the status of guard"""
        print("This is a max level guard.")


#  Inmate class
class Inmate:
    """A class modelling an inmate"""

    def __init__(self, Iname, gender, clothes, weapon, item):
        """Init statement"""
        self.Iname = Iname
        self.gender = gender
        self.clothes = clothes
        self.weapon = weapon
        self.item = item

    def describe_I(self):
        """Used to describe inmate"""
        print(f"This inmate is named {self.Iname}, they are {self.gender}.")

    def inventory(self):
        """Used to show what items are in inventory"""
        print(f"{self.Iname.upper()}'s Inventory:")
        print(f"\tClothes: {self.clothes}")
        print(f"\tWeapon: {self.weapon}")
        print(f"\tItems: {self.item}")
