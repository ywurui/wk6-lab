import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Create a fresh account before every test."""
        self.account = BankAccount(100, "Alice")

    def test_deposit_zero(self):
        self.account.deposit(0)
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

        self.assertEqual(self.account.balance, 100)

    def test_withdraw_zero(self):
        self.account.withdraw(0)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_positive_amount(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.balance, 60)

    def test_withdraw_entire_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(101)

        self.assertEqual(self.account.balance, 100)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

        self.assertEqual(self.account.balance, 100)

    def test_same_account_object(self):
        same_account = self.account
        self.assertIs(self.account, same_account)

    def test_different_account_objects(self):
        other_account = BankAccount(200, "Bob")
        self.assertIsNot(self.account, other_account)

    def test_different_accounts_with_same_attribute_values(self):
        other_account = BankAccount(100, "Alice")

        self.assertIsNot(self.account, other_account)
        self.assertEqual(self.account.balance, other_account.balance)
        self.assertEqual(self.account.name, other_account.name)


if __name__ == "__main__":
    unittest.main()
