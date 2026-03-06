class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}")

    def apply_discount(self, percent):
        """Returns the discounted price."""
        return self.price - (self.price * percent / 100)

# Creating objects and calling methods

p1 = Product("Laptop", 45000, "Electronics")
p2 = Product("Headphones", 2500, "Accessories")

p1.get_info()
p2.get_info()

# Testing discount method
print(f"Discounted {p1.name} Price: {p1.apply_discount(10)}")
