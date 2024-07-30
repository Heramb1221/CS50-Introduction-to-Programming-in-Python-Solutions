import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
    except ValueError:
        pass
    else:
        break

number = random.randrange(1, level)

while True:
    try:
        guess = input("Guess: ")
        if guess.isnumeric() or int(guess)>=1:
            if int(guess) == number:
                print("Just right!")
                break
            elif int(guess)>number:
                print("Too large!")
            else:
                print("Too small!")
        else:
            raise ValueError
    except ValueError:
        pass

