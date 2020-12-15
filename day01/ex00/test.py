from book import Book
from recipe import Recipe

livro = Book('Lucas')
r1 = Recipe('sandwich', 2, 10, ['ham', 'bread', 'cheese', 'tomatoes'],
            'lunch', 'put everything together, go to the fridge and tan dan')
r2 = Recipe('cake', 4, 60, ['flour', 'sugar', 'eggs'], 'dessert')
r3 = Recipe('salad', 1, 15, ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'lunch', 'cut everything and put in a bow')
livro.get_recipe_by_name('sandwich')
print()
livro.get_recipes_by_types('lunch')
print()
livro.add_recipe(r1)
livro.add_recipe(r2)
livro.add_recipe(r3)
livro.get_recipe_by_name('sandwich')
print()
livro.get_recipes_by_types('lunch')
print()
