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
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {result}")
        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {result:.2f}")
        elif choice == "5":
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

calculator()