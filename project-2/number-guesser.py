from random import randint

number = randint(1, 100)

no_of_guesses = 0

while True:
    no_of_guesses += 1
    guessed_number = input("Guess a number between 1 and 100: ") 

    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
        if guessed_number < 1 or guessed_number > 100:
            print("Please enter a number between 1 and 100.")
            continue
    else:
        print(f"'{guessed_number}' is not a valid number.")
        continue

    if guessed_number == number:
        print("Hurray! You guessed it correct this time")
        print(f"You guessed the number in {no_of_guesses} attempts.")
        play_again = input("Want to play again? (y/n) ")
        if (play_again.lower() == "y"):
            number = randint(1, 100)
            no_of_guesses = 0
            continue
        break

    if guessed_number < number:
        print("You were below the number.")
    else:
        print("You were above the number.")

print("Thanks for playing.")