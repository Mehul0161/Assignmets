def apply_discount(price, percent):
    """Returns the price after applying a percentage discount."""
    return price * (1 - percent / 100)

def flat_discount(price):
    """Returns the price after subtracting a flat discount of 50."""
    return price - 50
