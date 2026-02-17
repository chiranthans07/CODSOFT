def calculate(num1, num2, choice):
    
    if choice == "1":
        return num1 + num2
    
    elif choice == "2":
        return num1 - num2
    
    elif choice == "3":
        return num1 * num2
    
    elif choice == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero is not allowed."
    
    else:
        return "Invalid choice!"


print("===== Advanced Calculator =====")

while True:
    
    # Input validation using try-except
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.\n")
        continue
    
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    result = calculate(num1, num2, choice)
    
    print("Result:", result)
    
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    
    if again != "yes":
        print("Thank you for using the calculator!")
        break
