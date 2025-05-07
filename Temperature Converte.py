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
            
temperature_converter()
                