class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic Method for string representation
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator Overloading for '+'
    def __add__(self, other):
        return self.price + other.price

# Testing magic methods
p1 = Product("Mouse", 800, "Accessories")
p2 = Product("Keyboard", 1500, "Accessories")

print(p1)  # Uses __str__
print(f"Total Combined Price: ₹{p1 + p2}")  # Uses __add__
