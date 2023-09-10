
# Basic Calculator with Arbitrary Number of Arguments

# Function to add numbers
def add(*args):
    result = sum(args)
    return result

# Function to subtract numbers
def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

# Function to multiply numbers
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Function to divide numbers
def divide(*args):
    if 0 in args[1:]:
        return "Error! Division by zero."
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]

        if not numbers:
            print("No numbers entered. Please enter at least one number.")
            continue

        if choice == '1':
            print("Result:", add(*numbers))
        elif choice == '2':
            print("Result:", subtract(*numbers))
        elif choice == '3':
            print("Result:", multiply(*numbers))
        elif choice == '4':
            print("Result:", divide(*numbers))
    else:
        print("Invalid choice. Please enter a valid option.")
