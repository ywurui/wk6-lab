import unittest

from bank_account import BankAccount


class TestBankAccountG4(unittest.TestCase):
    def test_initial_balance_and_name(self):
        account = BankAccount(250, "Grace")
        self.assertEqual(account.balance, 250)
        self.assertEqual(account.name, "Grace")

    def test_default_constructor_values(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.name, "")

    def test_deposit_increases_balance(self):
        account = BankAccount(100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_deposit_zero_keeps_balance(self):
        account = BankAccount(100)
        account.deposit(0)
        self.assertEqual(account.balance, 100)

    def test_deposit_negative_amount_raises_error(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.deposit(-10)
        self.assertEqual(account.balance, 100)

    def test_withdraw_reduces_balance(self):
        account = BankAccount(100)
        account.withdraw(25)
        self.assertEqual(account.balance, 75)

    def test_withdraw_entire_balance(self):
        account = BankAccount(80)
        account.withdraw(80)
        self.assertEqual(account.balance, 0)

    def test_withdraw_zero_keeps_balance(self):
        account = BankAccount(100)
        account.withdraw(0)
        self.assertEqual(account.balance, 100)

    def test_withdraw_negative_amount_raises_error(self):
        account = BankAccount(100)
        with self.assertRaises(ValueError):
            account.withdraw(-5)
        self.assertEqual(account.balance, 100)

    def test_withdraw_more_than_balance_raises_error(self):
        account = BankAccount(50)
        with self.assertRaises(ValueError):
            account.withdraw(60)
        self.assertEqual(account.balance, 50)


if __name__ == "__main__":
    unittest.main()
