
import os

# --- Task 1: Write Sales Records to a File ---
print("--- Task 1: Write Sales Records to a File ---")
sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

print("Contents of sales_data.txt:")
with open("sales_data.txt", "r") as file:
    print(file.read())

# Extra: Comma-separated format
with open("sales_data_comma.txt", "w") as file:
    file.write(", ".join(map(str, sales)))
print("Extra: Data in comma-separated format stored in 'sales_data_comma.txt'.\n")

# --- Task 2: Read File in Different Ways ---
print("--- Task 2: Read File in Different Ways ---")
with open("sales_data.txt", "r") as file:
    print("Reading entire file using .read():")
    print(file.read())

with open("sales_data.txt", "r") as file:
    first_line = file.readline().strip()
    print(f"Reading first line using .readline(): {first_line}")

with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_integers = [int(line.strip()) for line in lines]
    print(f"Reading all lines and converting to integers: {sales_integers}\n")

# --- Task 3: Append New Sales ---
print("--- Task 3: Append New Sales ---")
new_sales = [5000, 2500, 1700]
with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

print("Updated contents of sales_data.txt:")
with open("sales_data.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())
print(f"Total number of lines: {len(content)}\n")

# --- Task 4: Generate Summary Report from File ---
print("--- Task 4: Generate Summary Report from File ---")
all_sales = []
with open("sales_data.txt", "r") as file:
    for line in file:
        all_sales.append(int(line.strip()))

total_sales = sum(all_sales)
highest_sale = max(all_sales)
lowest_sale = min(all_sales)
average_sale = total_sales / len(all_sales)

print(f"Total Sales: {total_sales}")
print(f"Highest Sale: {highest_sale}")
print(f"Lowest Sale: {lowest_sale}")
print(f"Average Sale: {average_sale:.2f}\n")

# --- Task 5: Create Product Info File (User Input) ---
print("--- Task 5: Create Product Info File (User Input) ---")
products = []
for i in range(1, 4):
    name = input(f"Enter Product {i} Name: ")
    price = input(f"Enter Price for {name}: ")
    products.append((name, price))

with open("products.txt", "w") as file:
    for name, price in products:
        file.write(f"{name} | {price}\n")

print("\nContents of products.txt:")
with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())
print("")

# --- Task 6: Read File Safely ---
print("--- Task 6: Read File Safely ---")
filename = input("Enter the filename to open: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(f"\n--- Reading {filename} ---")
        print(file.read())
else:
    print(f"File not found. Please check the filename: {filename}")
print("")

# --- Task 7: Mini Project - Export Discounted Prices ---
print("--- Task 7: Mini Project - Export Discounted Prices ---")
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter discount percentage (e.g., 10 for 10%): "))

with open("discount_report.txt", "w") as file:
    total_discounted_price = 0
    for product, original_price in prices.items():
        discounted_price = original_price * (1 - discount_percent / 100)
        total_discounted_price += discounted_price
        file.write(f"{product} | {original_price} | {discounted_price:.2f}\n")
    
    file.write("\n--- Summary ---\n")
    file.write(f"Total Items: {len(prices)}\n")
    file.write(f"Average Discounted Price: {total_discounted_price / len(prices):.2f}\n")

print("\nGenerating report in discount_report.txt...")
with open("discount_report.txt", "r") as file:
    print(file.read())
