
# Task 1: Product Collections (Lists & Tuples)
print("\n" + "="*35)
print(" TASK 1: PRODUCT COLLECTIONS ")
print("="*35)

products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]
sample_product = ("Laptop", 75000, "Electronics")

print(f"1. Products List: {products}")
print(f"2. Sample Product (Tuple): {sample_product}")
print(f"3. 2nd Product: {products[1]}")
print(f"4. Last Product: {products[-1]}")

products.append("Webcam")
products.append("Speakers")
print(f"5. Updated Products: {products}")

# Extra: Modification via conversion
temp_list = list(sample_product)
temp_list[1] = 72000
sample_product = tuple(temp_list)
print(f"6. Modified Sample Product: {sample_product}")


# Task 2: Categories (Sets)
print("\n" + "="*35)
print(" TASK 2: CATEGORIES (SETS) ")
print("="*35)

initial_categories = ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories", "Accessories", "Hardware", "Audio"]
categories_set = set(initial_categories)
print(f"1. Initial Categories Set: {categories_set}")

categories_set.add("Office Gear")
categories_set.add("Electronics") # Duplicate
print(f"2. After Adding 'Office Gear' & Duplicate: {categories_set}")

search_cat = "Electronics"
print(f"3. Does '{search_cat}' exist? {search_cat in categories_set}")
print(f"4. Total Unique Categories: {len(categories_set)}")


# Task 3: Product Pricing 
print("\n" + "="*35)
print(" TASK 3: PRODUCT PRICING ")
print("="*35)

price_dict = {
    "Laptop": 75000,
    "Smartphone": 45000,
    "Headphones": 5000,
    "Monitor": 12000,
    "Keyboard": 2500,
    "Mouse": 1500
}
print(f"1. Price Dictionary: {price_dict}")

# Updates
price_dict["Webcam"] = 3000
price_dict["Laptop"] = 72000
price_dict.pop("Mouse", None)
print(f"2. Dictionary after Updates: {price_dict}")

avg_price = sum(price_dict.values()) / len(price_dict)
print(f"3. Average Price: {avg_price:.2f}")

p_max = max(price_dict, key=price_dict.get)
p_min = min(price_dict, key=price_dict.get)
print(f"4. Max: {p_max} ({price_dict[p_max]}) | Min: {p_min} ({price_dict[p_min]})")


# Task 4: Combined Operations
print("\n" + "="*35)
print(" TASK 4: COMBINED OPERATIONS ")
print("="*35)

# Build Catalog
catalog = []
for i in range(len(products)):
    name = products[i]
    if name in price_dict:
        catalog.append((name, price_dict[name], initial_categories[i]))

print(f"1. Catalog (List of Tuples):")
for item in catalog: 
    print(f"   - {item}")

# Category Mapping
cat_map = {}
for name, price, cat in catalog:
    if cat not in cat_map: 
        cat_map[cat] = []
    cat_map[cat].append(name)

print("\n2. Category Mapping:")
for cat, items in cat_map.items(): 
    print(f"   - {cat}: {items}")

# Max Category
max_cat = max(cat_map, key=lambda k: len(cat_map[k]))
print(f"\n3. Category with most products: '{max_cat}'")
print(f"4. Products in '{max_cat}': {cat_map[max_cat]}")
