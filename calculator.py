# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b


def main():
    results = []  # store session results

    while True:
        print("\n===== Calculator Menu =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. View History")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            elif choice == "5":
                result = modulus(num1, num2)

            print(f"Result: {result}")
            results.append(result)

            # Save result to file
            with open("results.txt", "a") as f:
                f.write(str(result) + "\n")

        elif choice == "6":
            print("\n--- History ---")
            if results:
                for i, res in enumerate(results, 1):
                    print(f"{i}. {res}")
            else:
                print("No calculations yet.")

        elif choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
