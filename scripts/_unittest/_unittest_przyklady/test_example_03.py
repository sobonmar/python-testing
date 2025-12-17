# Fikstury
import time
import unittest

from example_02 import BankAccount


class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.test_start_time = time.time()

    @classmethod
    def tearDownClass(cls):
        print("tesarDownClass")
        duration = time.time() - cls.test_start_time
        print(f"Testy wykonały się w {duration} czasie")

    def setUp(self):
        print("setUp")
        self.account = BankAccount(initial_balance=100)

    def tearDown(self):
        print("tearDown")
        BankAccount.ACCOUNT_COUNTER = 0
        self.account = None  # można, ale nie trzeba

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)
        self.assertEqual(self.account.get_transaction_count(), 0)

    def test_deposit_success(self):
        self.account.deposit(100)

        self.assertEqual(self.account.balance, 200)
        self.assertEqual(self.account.get_transaction_count(), 1)
        self.assertIn("Deposit: +100", self.account.transaction_history)
        self.assertEqual(self.account.ACCOUNT_COUNTER, 1)

    def test_withdraw_success(self):
        self.account.withdraw(30)

        self.assertEqual(self.account.balance, 70)
        self.assertEqual(self.account.get_transaction_count(), 1)
        self.assertIn("Withdraw: -30", self.account.transaction_history)
        self.assertEqual(self.account.ACCOUNT_COUNTER, 1)
