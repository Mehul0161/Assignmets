from abc import ABC, abstractmethod

# --- Task 1 & 2: Basic Class, Constructor & Encapsulation ---
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # Private attribute (Encapsulation)
        self.category = category

    # Task 2: Getter & Setter
    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be positive.")

    # Task 1: Basic Method
    def get_info(self):
        print(f"Product: {self.name}, Price: ₹{self.__price}, Category: {self.category}")

    # Task 6: Magic Methods
    def __str__(self):
        return f"{self.name} ({self.category}) - ₹{self.__price}"

    def __add__(self, other):
        return self.__price + other.get_price()

    # Task 1 Extra: Discount method
    def apply_discount(self, percent):
        return self.__price - (self.__price * percent / 100)


# --- Task 3: Inheritance (Single-Level) ---
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    # Method Overriding
    def get_info(self):
        print(f"Electronic: {self.name}, Price: ₹{self.get_price()}, Warranty: {self.warranty_years} years")


# --- Task 4: Polymorphism ---
class Laptop(Product):
    def get_info(self):
        print(f"Laptop: {self.name} | Advanced Computing Power | Price: ₹{self.get_price()}")

class Mobile(Product):
    def get_info(self):
        print(f"Mobile: {self.name} | Portable Communication | Price: ₹{self.get_price()}")


# --- Task 5: Abstraction (Using Abstract Base Class) ---
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}...")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}...")


# --- Task 7: Mini Project (Inventory System) ---
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name.lower() != name.lower()]

    def get_total_value(self):
        return sum(p.get_price() for p in self.products)

    def show_all_products(self):
        for p in self.products:
            print(p)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        print(f"\nAdding product to {self.store_name}:")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        category = input("Enter category: ")
        self.inventory.add_product(Product(name, price, category))

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Value: ₹{self.inventory.get_total_value()}")


# --- Main Execution Block (Testing) ---
if __name__ == "__main__":
    print("=== Testing Task 4: Polymorphism ===")
    devices = [Laptop("MacBook Air", 85000, "laptop"), Mobile("Samsung S23", 75000, "mobile")]
    for d in devices:
        d.get_info()

    print("\n=== Testing Task 5: Abstraction ===")
    pay = UPIPayment()
    pay.process_payment(2000)

    print("\n=== Testing Task 6: Operator Overloading ===")
    p1 = Product("Mouse", 500, "Accessory")
    p2 = Product("Keyboard", 1000, "Accessory")
    print(f"Total Price: {p1 + p2}")

    print("\n=== Task 7: Mini Project Execution ===")
    my_store = Store("TuteDude Electronics")
    for _ in range(3):
        my_store.add_new_product()
    
    my_store.show_summary()
    my_store.inventory.show_all_products()
