def add(a, b):
    """Return the sum of a and b."""
    return a + b#testing changes
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
print("Calculator functions are ready to use.")
print("This is a simple calculator that can perform addition, subtraction, multiplication, and division.")
def calculator():
    print("Welcome to the simple calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"The result is: {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid input. Please try again.")