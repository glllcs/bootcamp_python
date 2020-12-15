import sys
from recipe import Recipe
import datetime


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name argument must be a string")
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.r_list = {'starter': [], 'lunch': [], 'dessert': []}

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("the argument must be a recipe")
        self.r_list[recipe.r_type].append(recipe)
        self.last_update = datetime.datetime.now()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rec_type in self.r_list:
            for recipes in self.r_list[rec_type]:
                if (recipes.name == name):
                    print(str(recipes))
                    return (recipes)
        print(f'{name} is not in {self.name} book')

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in self.r_list.keys():
            print("argument must be in ('starter', 'lunch', 'dessert')")
            return()
        print(f'{recipe_type} recipes:')
        for r in self.r_list[recipe_type]:
            print(r.name)
