import sys

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
       },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
       },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
       }
    }


def print_r(name):
    try:
        print('\n' + 21*'~', '\nRecipe for %s:' % name)
        print('Ingredients list:', cookbook[name]['ingredients'])
        print('To be eaten for %s.' % cookbook[name]['meal'])
        print('Takes', cookbook[name]['prep_time'], 'minutes of cooking.')
        print(21*'~' + '\n')
    except KeyError:
        print("\n'%s' didn't matched with any recipe registered.\n" % name)
    return()


def delete_r(name):
    try:
        del cookbook[name]
        print('\nDeleted recipe for %s\n' % name)
    except KeyError:
        print("\n'%s' didn't matched with any recipe registered.\n" % name)
    return()


def print_c():
    print('\n' + 21*'~', '\nRegistered recipes:')
    for p_recipe in cookbook:
        print('~', p_recipe)
    print(21*'~' + '\n')


def add_r(name, ingr, meal, time):
    cookbook[name] = {
        'ingredients': ingr,
        'meal': meal,
        'prep_time': time
        }
    print("\nNew recipe registered: %s.\n" % name)


print('\n' + 21*'~', "Lucas' Cookbook", 21*'~')
while True:
    print('Please select an option by typing the corresponding number:\n'
          '1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n'
          '4: Print the cookbook\n5: Quit')
    option = input('>> ')
    if option == '1':
        print("\nPlease enter the new recipe's name:")
        name = input('>> ')
        print("\nPlease enter %s's number of ingredients:" % name)
        nbr_ing = int(input('>> '))
        print("\nPlease enter %s's ingredients:" % name)
        ingr = []
        while (nbr_ing > 0):
            ingr.append(input('>> '))
            nbr_ing -= 1
        print("\nPlease enter %s's meal type:" % name)
        meal = input('>> ')
        print("\nPlease enter %s's preparation time (minutes):" % name)
        time = input('>> ')
        add_r(name, ingr, meal, time)
    elif option == '2':
        print("\nPlease enter the recipe's name to delete it:")
        delete_r(input('>> '))
    elif option == '3':
        print("\nPlease enter the recipe's name to get its details:")
        print_r(input('>> '))
    elif option == '4':
        print_c()
    elif option == '5':
        print(59*'~')
        print('Cookbook closed.')
        exit()
    else:
        print('\nThis option does not exist, please type the corresponding'
              ' number.')
        print('To exit, enter 5.\n')
