# Demonstrating doctest best practices + sposoby uruchamiania
"""
Demonstration module with BankAccount class and helper functions.

Module-level usage examples:
"""
import doctest


class BankAccount:
    """
    Represents a bank account.
    """

    def __init__(self, account_number, initial_balance=0.0):
        """Initialize new bank account.

        Args:
            account_number: Unique identifier for the account
            initial_balance: Starting balance (default 0.0)

        """
        self.account_number = account_number
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money to account.

        Args:
            amount: Amount to deposit (must be positive)

        Returns:
            Updated balance after deposit

        Raises:
            ValueError: If amount is not positive

        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from account.

        Args:
            amount: Amount to withdraw (must be positive)

        Returns:
            Updated balance after withdrawal

        Raises:
            ValueError: If amount is not positive or exceeds balance

        75.0
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Return current balance.

        Returns:
            Current account balance

        """
        return self.balance


def validate_email(email):
    """
    Validate email address (simplified version).

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email is valid

    Examples:

    """
    import re
    if not email or not isinstance(email, str):
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
