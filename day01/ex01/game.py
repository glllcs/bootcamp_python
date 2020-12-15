class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print("!!!", self.house_words, "!!!")


class Stark(GotCharacter):
    """You were born in the long summer, you've never known anything else. \
But now winter is truly coming. In the winter, we must protect ourselves, \
look after one another"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"


class Lannister(GotCharacter):
    """You have to give it to the Lannisters – they may be the most pompous, \
ponderous cunts the gods ever suffered to walk the world, but they do have \
outrageous amounts of money"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"


class Targaryen(GotCharacter):
    """Half the Targaryens went mad, didn't they? What's the saying? 'Every \
time a Targaryen is born the gods flip a coin"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and Blood"
