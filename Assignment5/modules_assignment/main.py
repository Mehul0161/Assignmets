# Main application to test modules and packages

# Task 1: Importing math_utils module
import math_utils
from math_utils import square

print("--- Testing math_utils module ---")
print(f"5 + 3 = {math_utils.add(5, 3)}")
print(f"10 - 4 = {math_utils.subtract(10, 4)}")
print(f"Square of 6 = {square(6)}\n")


# Task 2: Importing string_utils module
import string_utils

print("--- Testing string_utils module ---")
text = "hello world"
print(f"Capitalized: {string_utils.capitalize_words(text)}")
print(f"Reversed: {string_utils.reverse_string(text)}")
print(f"Word count: {string_utils.word_count(text)}\n")


# Task 4: Importing and testing shop_package
import shop_package.discount as disc
from shop_package.billing import calculate_total

print("--- Testing shop_package package ---")
# Using disc alias for apply_discount
original_price = 1000
discounted_price = disc.apply_discount(original_price, 10)
print(f"Original Price: {original_price}, Discounted Price (10%): {discounted_price}")

# Testing flat_discount directly from the package (if exported via __init__.py)
# Or by explicitly importing it.
import shop_package # This works because we added functions in __init__.py
print(f"Flat Discount on 500: {shop_package.flat_discount(500)}")

# Testing calculate_total and apply_tax from billing
items_prices = [100, 200, 300]
total_amount = calculate_total(items_prices)
total_with_tax = shop_package.apply_tax(total_amount)

print(f"Items: {items_prices}")
print(f"Total Amount: {total_amount}")
print(f"Total with 5% tax: {total_with_tax:.2f}")
