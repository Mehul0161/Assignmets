class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price  # Private attribute (Encapsulation)
        self.category = category

    # Getter method
    def get_price(self):
        return self.__price

    # Setter method with validation
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Error: Price must be greater than 0.")

    def get_info(self):
        print(f"Product: {self.name}, Price: {self.__price}, Category: {self.category}")

# Testing encapsulation and modifying price using setter
p1 = Product("Smartphone", 15000, "Electronics")
print(f"Original Price: {p1.get_price()}")

p1.set_price(16000)  # Valid update
print(f"Updated Price: {p1.get_price()}")

p1.set_price(-500)   # Invalid update
p1.get_info()
