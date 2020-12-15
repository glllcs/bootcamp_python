import sys


class Recipe:
    def __init__(self, name, c_lvl, c_time, ing, r_type, desc=""):
        if (not isinstance(name, str) or not name):
            raise TypeError("name argument must be a string")
        if (not isinstance(c_lvl, int) or c_lvl < 1 or c_lvl > 5):
            raise TypeError("c_lvl argument must be an integer from 1 to 5")
        if (not isinstance(c_time, int) or c_time < 0):
            raise TypeError("c_time argument must be a positive integer")
        if (not isinstance(ing, list) or not ing[0]):
            raise TypeError("ing argument must be a not empty list")
        if (not isinstance(r_type, str) or r_type not in
           ('starter', 'lunch', 'dessert')):
            raise TypeError("r_type argument must be in ('starter', 'lunch', "
                            "dessert')")
        if (not isinstance(desc, str)):
            raise TypeError("desc argument must be a string")
        self.name = name
        self.c_lvl = c_lvl
        self.c_time = c_time
        self.ing = ing
        self.desc = desc
        self.r_type = r_type

    def __str__(self):
        txt = f'--> {self.name.capitalize()} <--\n'\
              f'Cooking level: {self.c_lvl}\n'\
              f'Ingredients list:\n'
        for i in self.ing:
            txt += '\t- ' + i + '\n'
        txt += f'To be eaten for {self.r_type}.\n'\
               f'Takes {self.c_time} minutes of cooking.\n'
        if self.desc:
            txt += f'Description: {self.desc}.\n'
        return(txt)
