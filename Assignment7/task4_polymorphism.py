class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Generic Product: {self.name}")

class Laptop(Product):
    def get_info(self):
        print(f"Laptop Model: {self.name}, Price: {self.price}, Category: {self.category}")

class Mobile(Product):
    def get_info(self):
        print(f"Mobile Device: {self.name}, Price: {self.price}, Category: {self.category}")

# Demonstrating polymorphism using a loop
products = [
    Laptop("Dell XPS", 95000, "Computers"),
    Mobile("iPhone 15", 79000, "Phones")
]

for prod in products:
    prod.get_info()  # Calls overridden method for each object
