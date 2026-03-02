
# Task 1: Safe Division Utility
print("--- Task 1: Safe Division Utility ---")
try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))
    result = num / den
except ValueError:
    print("Error: Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Operation Complete\n")

# Task 2: Bill Calculator with Error Handling
print("--- Task 2: Bill Calculator ---")
prices = [120, 350, 'abc', 500, -200, 800]
total = 0
for p in prices:
    try:
        if not isinstance(p, (int, float)):
            raise TypeError("Not a number")
        if p < 0:
            raise ValueError("Negative price not allowed")
        total += p
    except TypeError:
        print(f"Skipping invalid item: {p} (Type Error)")
    except ValueError as e:
        print(f"Skipping invalid item: {p} ({e})")
print(f"Running total: {total}\n")

# Task 3: Custom Exception: Age Validator
print("--- Task 3: Age Validator ---")
def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return age

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print(f"Age {user_age} is valid.")
except ValueError as e:
    print(f"Error: {e}\n")

# Task 4: File Reader with Exception Handling
print("--- Task 4: File Reader ---")
filename = input("Enter filename to read: ")
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
        print("First 3 lines:")
        for line in lines[:3]:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File operation attempted.\n")

# Task 5: Mini Program: Safe Shopping Cart
print("--- Task 5: Safe Shopping Cart ---")
cart = []
while True:
    val = input("Enter price (or 'q' to quit): ")
    if val.lower() == 'q':
        break
    try:
        price = float(val)
        if price < 0:
            raise ValueError("Price cannot be negative")
        cart.append(price)
    except ValueError as e:
        if "negative" in str(e):
            print(f"Error: {e}")
        else:
            print("Error: Invalid input, please enter a number.")

print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart)}")
