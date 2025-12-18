"""Simple calculator module for coverage demonstration"""


def add(a, b):
    """Add two numbers"""
    return a + b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_positive(number):
    """Check if number is positive"""
    if number > 0:
        return True
    else:
        return False


def get_grade(score):
    """Convert score to letter grade"""
    if score < 0:
        raise ValueError("Score cannot be negative")

    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "F"
