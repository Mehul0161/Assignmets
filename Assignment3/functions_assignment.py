# Task 1: Basic Function: Price After Discount
def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60
    return price - (price * (discount_percent / 100))

print("--- Task 1: Basic Function ---")
print(f"1000 with 10% discount: {apply_discount(1000, 10)}")
print(f"500 with default discount: {apply_discount(500)}")

# Task 2: Recursive Function: Factorial Utility
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\n--- Task 2: Recursive Function ---")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
print(f"Factorial of -3: {factorial(-3)}")

# Task 3: Lambda Function: GST Calculator
gst = lambda price: price + (0.18 * price)
final_price = lambda price, discount: gst(apply_discount(price, discount))

print("\n--- Task 3: Lambda Function ---")
print(f"Price 100 with GST: {gst(100)}")
print(f"Price 1000 with 10% discount + GST: {final_price(1000, 10)}")

# Task 4: Using map(): Apply GST to List of Prices
prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices))

print("\n--- Task 4: Using map() ---")
print(f"Original prices: {prices}")
print(f"Prices after GST: {prices_with_gst}")

# Task 5: Using filter(): Filter Expensive Products
prices_list = [100, 250, 400, 1200, 50, 2000, 850]
expensive = list(filter(lambda p: p > 500, prices_list))
affordable = list(filter(lambda p: p <= 500, prices_list))

print("\n--- Task 5: Using filter() ---")
print(f"Greater than 500: {expensive}")
print(f"Less than or equal to 500: {affordable}")

# Task 6: Combined Utility Function
def process_prices(prices_input):
    discounted = list(map(lambda p: p * 0.9, prices_input))
    filtered = list(filter(lambda p: p > 300, discounted))
    return discounted, filtered

print("\n--- Task 6: Combined Utility ---")
all_disc, high_val = process_prices([100, 500, 900, 50, 750])
print(f"All discounted (10% off): {all_disc}")
print(f"Discounted prices > 300: {high_val}")

# Task 7: Mini Problem: Menu Using Functions
def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if not prices_list: return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if not prices_list: return 0
    return max(prices_list)

print("\n--- Task 7: Menu Driven Utility ---")
menu_prices = []
while True:
    print("\n[1] Add [2] Average [3] Max [q] Quit")
    choice = input("Choice: ").lower()
    
    if choice == 'q':
        break
    elif choice == '1':
        p_val = input("Price: ")
        if p_val.replace('.','',1).isdigit():
            add_price(menu_prices, float(p_val))
        else:
            print("Invalid input.")
    elif choice == '2':
        print(f"Average: {get_average_price(menu_prices):.2f}")
    elif choice == '3':
        print(f"Maximum: {get_max_price(menu_prices)}")
    else:
        print("Invalid choice.")
