class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}")

# Subclass inheriting from Product
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # Overriding the get_info method
    def get_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Category: {self.category}, Warranty: {self.warranty_years} years")

# Demonstrating inheritance and overriding
e1 = ElectronicProduct("Washing Machine", 25000, "Appliances", 2)
e1.get_info()
