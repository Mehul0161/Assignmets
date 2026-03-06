from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Subclass for Credit Card
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ₹{amount}...")

# Subclass for UPI
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}...")

# Testing abstract classes and implementation
payments = [CreditCardPayment(), UPIPayment()]

for p in payments:
    p.process_payment(5000)
