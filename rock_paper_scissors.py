import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    rounds_played = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'exit' to stop playing.\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice == "exit":
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        rounds_played += 1

        if result == "user":
            print("You win this round!\n")
            user_wins += 1
        elif result == "computer":
            print("Computer wins this round!\n")
            computer_wins += 1
        else:
            print("It's a draw!\n")

    print("Game Over!")
    print(f"Total rounds played: {rounds_played}")
    print(f"Your wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")

if __name__ == "__main__":
    play_game()
