# Assignment 2: Python - Control Flow (Conditionals & Loops)

This assignment focuses on control flow structures in Python, including `if/elif/else`, `for` loops, `while` loops, and loop control statements (`break`, `continue`).

## Project Structure
- `control_flow_assignment.py`: Main script containing all assignment tasks.
- `README.md`: Documentation on how the project works and how to run it.

## How to Run the Assignment

The script is interactive and combines all tasks into one executable file. 

To run it, open your terminal and type:
```bash
python control_flow_assignment.py
```

### Tasks Summary:

- **Task 1: Discount Rules (if/elif/else)**  
  Reads an integer `order_amount`, applies discount logic (15% for >=2000, 10% for >=1500, 7% for >=1000), and calculates a 5% tax.
  
- **Task 2: Process Multiple Orders (for loop)**  
  Processes `orders = [1200, 2500, 800, 1750, 3000]`, displays results in a summary table, and computes total revenue.
  
- **Task 3: User Menu (while loop + break/continue)**  
  An interactive CLI menu where you can:
  - Add orders to a running list.
  - View all orders and their totals after discounts.
  - Quit the menu.
  
- **Task 5: Loop Control (break & continue)**  
  Iterates through daily sales `[200, 150, 0, 400, 50, -1, 300]`. It uses `continue` to skip zero sales and `break` when it encounters corrupted data (-1).

## Restrictions & Constraints
- No functions, classes, or external libraries were used, as per the assignment guidelines.
- Developed strictly using Python's core control flow constructs.
