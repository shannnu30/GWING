import random

quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. Roald Dahl", "D. Dan Brown"],
        "answer": "B"
    },
    {
        "question": "What is 7 x 8?",
        "options": ["A. 56", "B. 64", "C. 48", "D. 54"],
        "answer": "A"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    for index, q in enumerate(quiz_questions):
        print(f"Question {index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    print(f"Your final score is {score} out of {len(quiz_questions)}")

def number_guessing_game():
    print("\nBonus Game: Number Guessing Game")
    print("I have selected a number between 1 and 20. Try to guess it!")

    number_to_guess = random.randint(1, 20)
    attempts = 0
    guessed = False

    while not guessed and attempts < 5:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print("Congratulations! You guessed it correctly.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

    if not guessed:
        print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")

def main():
    run_quiz()
    play_guess = input("\nDo you want to play the Number Guessing Game? (yes/no): ").strip().lower()
    if play_guess == "yes":
        number_guessing_game()
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
