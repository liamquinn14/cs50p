import random

while True:
    try:
        max_range = int(input("Level: "))
        if max_range < 1:
            continue
        else:
            break
    except EOFError:
        print("Game terminated.")
        break
    except ValueError:
        print("Invalid integer provided.")
        continue

number_to_guess = random.randint(1, max_range)

while True:
    try:
        next_guess = int(input("Guess: "))
        if next_guess < 1:
            continue
        elif next_guess > number_to_guess:
            print("Too high!")
            continue
        elif next_guess < number_to_guess:
            print("Too low!")
            continue
        else:
            print("Correct!")
            break
    except EOFError:
        print("Game terminated.")
        break
    except ValueError:
        print("Invalid integer provided.")
        continue
