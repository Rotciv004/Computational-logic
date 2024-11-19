def add(base, num1, num2):
    return base_converter(base, int(num1, base) + int(num2, base))

def subtract(base, num1, num2):
    return base_converter(base, int(num1, base) - int(num2, base))

def multiply_by_digit(base, num, digit):
    return base_converter(base, int(num, base) * int(digit, base))

def divide_by_digit(base, num, digit):
    return base_converter(base, int(num, base) // int(digit, base))

def convert_substitution(base_from, base_to, number):
    return base_converter(base_to, int(str(number), base_from))

def successive_divisions(base, number):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result

def base_converter(base, value):
    if base == 10:
        return str(value)
    elif base == 2:
        return bin(value)[2:]
    elif base == 8:
        return oct(value)[2:]
    elif base == 16:
        return hex(value)[2:]


def show_menu():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication by digit")
    print("4. Division by digit")
    print("5. Convert using Substitution Method")
    print("6. Convert using Successive Divisions")
    print("0. Exit")

def get_user_input():
    base_from = int(input("Enter the base for operations (2, 8, 16): "))
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    return base_from, num1, num2

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif 1 <= choice <= 4:
            base_from, num1, num2 = get_user_input()

            if choice == 1:
                print(f"Result: {add(base_from, num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract(base_from, num1, num2)}")
            elif choice == 3:
                digit = input("Enter the digit for multiplication: ")
                print(f"Result: {multiply_by_digit(base_from, num1, digit)}")
            elif choice == 4:
                digit = input("Enter the digit for division: ")
                print(f"Result: {divide_by_digit(base_from, num1, digit)}")
        elif choice == 5:
            base_from, base_to = int(input("Enter the base for conversion (2, 8, 16): ")), int(input("Enter the target base for conversion (2, 8, 16): "))
            num1 = input("Enter the number to convert: ")
            print(f"Result: {convert_substitution(base_from, base_to, num1)}")
        elif choice == 6:
            base_from = int(input("Enter the base for conversion (2, 8, 16): "))
            num1 = input("Enter the number to convert: ")
            print(f"Result: {successive_divisions(base_from, int(num1, base_from))}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
