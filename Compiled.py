# All-In-One Simple Program Suite

import random

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2:.2f}")
        elif choice == "5":
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

def temperature_converter():
    while True:
        print("\nTemperature Converter Menu:")
        print("1. Convert Celsius to Fahrenheit ")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            c = float(input("Enter Celcius: "))
            f = (c * 9/5) + 32
            print("Fahrenheit: ", f)
        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print("Celcius: ", c)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid Choice. Try again.")

def todo_list():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task to add:")
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == "3":
            if tasks:
                print("Your Tasks:")
                for t in tasks:
                    print("-", t)
            else:
                print("No tasks in the list.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

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

def grade_calculator():
    subjects = []

    while True:
        print("\n1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            subject = input("Enter the subject: ")
            score_input = input("Enter the score: ")

            if score_input.isdigit():
                score = int(score_input)
                subjects.append(score)
                print("Score added.")
            else:
                print("Invalid score. Please enter a number.")

        elif choice == "2":
            if subjects:
                average = sum(subjects) / len(subjects)
                print(f"Average Grade: {average:.2f}")
            else:
                print("No scores added yet.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Calculator")
        print("2. Temperature Converter")
        print("3. To-Do List")
        print("4. Number Guessing Game")
        print("5. Grade Calculator")
        print("6. Exit")

        main_choice = input("Enter your choice (1-6): ")

        if main_choice == "1":
            calculator()
        elif main_choice == "2":
            temperature_converter()
        elif main_choice == "3":
            todo_list()
        elif main_choice == "4":
            number_guessing_game()
        elif main_choice == "5":
            grade_calculator()
        elif main_choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")

main_menu()