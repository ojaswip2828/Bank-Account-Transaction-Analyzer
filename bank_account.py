"""

Features:
- BankAccount class with deposit, withdraw, balance check
- Transaction history stored as a list of dicts
- Export transaction history to a CSV (for the pandas analysis script)
- Simple text menu to interact with the account
"""

import pandas as pd
from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []  

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self._log_transaction("deposit", amount)
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self._log_transaction("withdraw", amount)
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def _log_transaction(self, ttype, amount):
        self.history.append({
            "owner": self.owner,
            "type": ttype,
            "amount": amount,
            "balance_after": self.balance,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def print_history(self):
        if not self.history:
            print("No transactions yet.")
            return
        for t in self.history:
            print(f"{t['date']} | {t['type']:8} | amount: {t['amount']:>8} | balance after: {t['balance_after']}")

    def export_to_csv(self, filename="transactions.csv"):
        if not self.history:
            print("No transactions to export.")
            return
        df = pd.DataFrame(self.history)
        df.to_csv(filename, index=False)
        print(f"Exported {len(self.history)} transactions to {filename}")


def menu():
    owner = input("Enter account owner name: ")
    account = BankAccount(owner)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. View transaction history")
        print("5. Export history to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            print(f"Current balance: {account.get_balance()}")
        elif choice == "4":
            account.print_history()
        elif choice == "5":
            account.export_to_csv()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
