print("\n--- Task 1: Discount Rules ---")
order_input = input("Enter integer order amount for Task 1: ")

if not order_input.lstrip('-').isdigit():
    print("Error: Invalid input. Input must be an integer. Exiting Task 1.")
else:
    order_amount = int(order_input)
    discount_pct = 0
    
    if order_amount >= 2000:
        discount_pct = 15
    elif order_amount >= 1500:
        discount_pct = 10
    elif order_amount >= 1000:
        discount_pct = 7
    else:
        discount_pct = 0
    
    discount_amount = (discount_pct / 100) * order_amount
    subtotal = order_amount - discount_amount
    
    tax = subtotal * 0.05
    final_total = subtotal + tax
    
    print(f"Applied Discount: {discount_pct}%")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Final Total: {final_total:.2f}")


print("\n--- Task 2: Process Multiple Orders ---")
orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders_count = 0

print(f"{'Order Amount':<15} -> {'Discount%':<10} -> {'Final Amount':<15}")
print("-" * 45)

for amount in orders:
    discount_pct = 0
    if amount >= 2000:
        discount_pct = 15
    elif amount >= 1500:
        discount_pct = 10
    elif amount >= 1000:
        discount_pct = 7
    
    discount_amount = (discount_pct / 100) * amount
    final_amount = amount - discount_amount
    
    if discount_pct > 0:
        discounted_orders_count += 1
        
    total_revenue += final_amount
    print(f"{amount:<15} -> {str(discount_pct) + '%':<10} -> {final_amount:<15.2f}")

print("-" * 45)
print(f"Total revenue after discounts: {total_revenue:.2f}")
print(f"Orders with discount: {discounted_orders_count}")


print("\n--- Task 3: User Menu ---")
user_orders = []

while True:
    print("\nMenu: [1] Add Order [2] Show Summary [q] Quit")
    choice = input("Choice: ").lower()
    
    if choice == 'q':
        break
    
    elif choice == '1':
        amt_in = input("Enter amount: ")
        if amt_in.lstrip('-').isdigit():
            user_orders.append(int(amt_in))
        else:
            print("Invalid input.")
            continue
            
    elif choice == '2':
        if not user_orders:
            print("List is empty.")
            continue
        
        print(f"{'Amount':<10} | {'Discount%':<10} | {'Final Amount':<10}")
        current_total = 0
        for amt in user_orders:
            pct = 0
            if amt >= 2000: pct = 15
            elif amt >= 1500: pct = 10
            elif amt >= 1000: pct = 7
            
            final = amt - (pct/100 * amt)
            current_total += final
            print(f"{amt:<10} | {str(pct)+'%':<10} | {final:<10.2f}")
        print(f"Grand Total: {current_total:.2f}")
        
    else:
        print("Invalid choice.")
        continue


print("\n--- Task 5: Loop Control ---")
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily:
    if sale == -1:
        print(f"Stopped: Corrupted data ({sale})")
        break
    
    if sale == 0:
        continue
    
    total_sales += sale
    print(f"Sale: {sale} | Running Total: {total_sales}")

print(f"Final Total: {total_sales}")
