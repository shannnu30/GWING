import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    # Loop until the user guesses correctly
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.\n")
            elif guess > number_to_guess:
                print("Too high. Try again.\n")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed = True

        except ValueError:
            print("Invalid input. Please enter a number.\n")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
