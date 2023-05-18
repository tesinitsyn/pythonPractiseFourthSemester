import deal
import pytest


@deal.inv(lambda self: self.balance >= 0)
class BankAccount:
    def __init__(self, account_number: str, balance: float = 0):
        self.account_number = account_number
        self.balance = balance

    @deal.pre(lambda self, amount: amount > 0)
    @deal.post(
        lambda self, amount, result: result == f"{amount} средств успешно зачислены на счет {self.account_number}")
    def deposit(self, amount: float) -> str:
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    @deal.pre(lambda self, amount: 0 < amount <= self.balance)
    @deal.post(lambda self, amount, result: result == f"{amount} средств успешно сняты с счета {self.account_number}")
    def withdraw(self, amount: float) -> str:
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self) -> str:
        return f"Баланс счета {self.account_number}: {self.balance}"


def test_bank_account_withdraw_error():
    account = BankAccount("123", 100)
    with pytest.raises(deal.PreContractError):
        account.withdraw(200)


def test_bank_account_negative_balance_error():
    with pytest.raises(deal.InvContractError):
        account = BankAccount("123", -100)
