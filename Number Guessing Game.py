import random

def number_guessing_game():
    while True:
        print("\n1. Play Number Guessing Game")
        print("2. Exit")

        choice = input("Enter choice (1-2): ")

        if choice == "1":
            number = random.randint(1, 100)
            attempts = 0

            while True:
                guess = input("Guess the number (1-100): ")
                if not guess.isdigit():
                    print("Please enter a valid number.")
                    continue

                guess = int(guess)
                attempts += 1

                if guess < number:
                    print("Too low!")
                elif guess > number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

number_guessing_game()