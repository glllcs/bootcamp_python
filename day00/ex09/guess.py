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
    if n_guess == 1 and num == 42 and guess == 42:
        print("The answer to the ultimate question of life, the universe "
              "and everything is 42.\nCongratulations! You got it on your "
              "first try!")
        exit()
    elif guess == num:
        print("Congratulations, you've got it!\nYou won in %d attempts!"
              % n_guess)
        exit()
    elif guess < num:
        print("Too low!")
    else:
        print("Too high!")
