#  This is a file for classes, these include character classes so far


class Player:
    """A class to describe player"""

    def __init__(self, name):
        """The init statement"""
        self.name = name

    def say_name(self):
        """Will print players name"""
        print(f"Your players name is {self.name.upper()}.")


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


class Captain(Guard):
    """Class modelling a guard captain"""

    def __init__(self, gname):
        """Init statement"""
        super().__init__(gname)

    def status(self):
        """Shows the status of guard"""
        print("This is a max level guard.")
