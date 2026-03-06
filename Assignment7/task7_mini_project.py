class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - ₹{self.price}"

    def __add__(self, other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        self.products = [p for p in self.products if p.name.lower() != name.lower()]

    def get_total_value(self):
        return sum(p.price for p in self.products)

    def show_all_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for p in self.products:
                print(p)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        new_prod = Product(name, price, category)
        self.inventory.add_product(new_prod)

    def show_summary(self):
        print(f"\n--- {self.store_name} Summary ---")
        print(f"Total Items: {len(self.inventory.products)}")
        print(f"Total Inventory Value: ₹{self.inventory.get_total_value()}\n")

# Main execution logic for Task 7 requirements
if __name__ == "__main__":
    # 1. Creating a Store object
    my_store = Store("ElectroHub")

    # 2. Adding 3 products (using the interactive method as per prompt request)
    print("Add 3 products to the store:")
    for _ in range(3):
        my_store.add_new_product()

    # 3. Showing summary
    my_store.show_summary()
    my_store.inventory.show_all_products()

    # 4. Using __add__ to combine prices of two products
    if len(my_store.inventory.products) >= 2:
        p1 = my_store.inventory.products[0]
        p2 = my_store.inventory.products[1]
        print(f"\nCombined price of {p1.name} and {p2.name}: ₹{p1 + p2}")
