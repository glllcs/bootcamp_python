from random import randint

num = randint(1, 99)
print("This is an interactive guessing game!\nYou have to enter a number "
      "between 1 and 99 to find out the secretnumber.\n"
      "Type 'exit' to end the game.\nGood luck!\n")

n_guess = 0
while (True):
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    if guess == "exit":
        print("Goodbye")
        exit()
    n_guess += 1
    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number.")
        continue
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        if num == 42:
            print("The answer to the ultimate question of life, the universe "
                  "and everything is 42.")
        if n_guess == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!\nYou won in %d attempts!"
                  % n_guess)
        exit()
