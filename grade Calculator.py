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
        
grade_calculator()