def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. Two paths lie ahead of you.")
    print("1. Take the left path")
    print("2. Take the right path")

    choice1 = input("Enter 1 or 2: ")

    if choice1 == "1":
        left_path()
    elif choice1 == "2":
        right_path()
    else:
        print("Invalid choice. The forest swallows you. Game Over.")

def left_path():
    print("\nYou took the left path and found a river.")
    print("1. Try to swim across")
    print("2. Look for a bridge")

    choice2 = input("Enter 1 or 2: ")

    if choice2 == "1":
        print("\nThe current was too strong. You drowned. Game Over.")
    elif choice2 == "2":
        print("\nYou found a bridge and safely crossed the river.")
        print("On the other side, you find a treasure chest. You win!")
    else:
        print("Invalid choice. You slip and fall into the river. Game Over.")

def right_path():
    print("\nYou took the right path and encountered a sleeping bear.")
    print("1. Try to sneak past the bear")
    print("2. Throw a rock to distract it")

    choice3 = input("Enter 1 or 2: ")

    if choice3 == "1":
        print("\nYou successfully sneak past the bear.")
        print("You find a cave with gold inside. You win!")
    elif choice3 == "2":
        print("\nThe bear wakes up and chases you. You couldn't escape. Game Over.")
    else:
        print("Invalid choice. The bear wakes up and attacks you. Game Over.")

# Run the game
if __name__ == "__main__":
    start_adventure()
