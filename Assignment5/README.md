
# Assignment 5: Importing, Creating Modules & Packages

This assignment demonstrates how to organize code into modules and packages for better reusability and scalability in Python.

## Folder Structure
```
modules_assignment/
  main.py                 <- Entry point for testing all modules and packages
  math_utils.py           <- Simple math operations (Task 1)
  string_utils.py         <- Basic string manipulations (Task 2)
  shop_package/           <- Package for retail operations (Task 3)
    __init__.py           <- Exposes package functions for direct access
    discount.py           <- Discount calculation functions
    billing.py            <- Billing and tax calculation functions
```

## How to Run
1. Open a terminal/command prompt.
2. Navigate to the `modules_assignment/` directory.
3. Run the following command:
   ```bash
   python main.py
   ```

## Key Tasks & Concepts
- **Task 1: Creating a Module** - Implemented basic math functions in `math_utils.py`.
- **Task 2: Creating Another Module** - Implemented string utilities in `string_utils.py`.
- **Task 3: Creating a Package** - Structured the `shop_package/` with multiple modules and a package initializer.
- **Task 4: Package Importing** - Demonstrated various ways to import from sub-modules and using aliases.
