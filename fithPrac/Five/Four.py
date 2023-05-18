import sqlite3
import unittest

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        return f"Баланс счета {self.account_number}: {balance}"

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"


import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account_number = 1234567890
        self.account = BankAccount(self.account_number)

    def tearDown(self):
        self.account.close_account()
        self.account = None

    def test_open(self):
        balance = 1000.0
        self.account.create_account(balance)
        self.assertEqual(self.account.check_balance(), f"Баланс счета {self.account_number}: {balance}")

    def test_deposit(self):
        balance = 1000.0
        self.account.create_account(balance)
        amount = 500.0
        self.account.deposit(amount)
        self.assertEqual(self.account.check_balance(), f"Баланс счета {self.account_number}: {balance + amount}")

    def test_withdraw(self):
        balance = 1000.0
        self.account.create_account(balance)
        amount = 500
        self.account.withdraw(amount)
        self.assertEqual(self.account.check_balance(), f"Баланс счета {self.account_number}: {balance - amount}")

    def test_check_balance(self):
        balance = 1000.0
        self.account.create_account(balance)
        self.assertEqual(self.account.check_balance(), f"Баланс счета {self.account_number}: {balance}")

    def test_close(self):
        balance = 1000.0
        self.account.create_account(balance)
        self.account.close_account()
        self.assertRaises(sqlite3.Error, self.account.check_balance)