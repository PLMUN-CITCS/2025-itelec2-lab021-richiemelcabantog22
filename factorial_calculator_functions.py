def get_non_negative_integer():
    while True:
        user_input = input("Please enter a non-negative integer: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()