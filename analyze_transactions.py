"""
Analyze the transactions.csv exported by bank_account.py using pandas.

Run bank_account.py first, do a few deposits/withdrawals, choose
option 5 to export, then run this script.
"""

import pandas as pd

FILENAME = "transactions.csv"


def analyze(filename=FILENAME):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"{filename} not found. Run bank_account.py first and export history (option 5).")
        return

    print("=== Transaction Summary ===")
    print(f"Total transactions: {len(df)}")

    total_deposits = df[df["type"] == "deposit"]["amount"].sum()
    total_withdrawals = df[df["type"] == "withdraw"]["amount"].sum()

    print(f"Total deposited: {total_deposits}")
    print(f"Total withdrawn: {total_withdrawals}")
    print(f"Average transaction size: {df['amount'].mean():.2f}")
    print(f"Largest transaction: {df['amount'].max()}")

    print("\n=== By Transaction Type ===")
    print(df.groupby("type")["amount"].agg(["count", "sum", "mean"]))

    print("\n=== Last 5 Transactions ===")
    print(df.tail(5))


if __name__ == "__main__":
    analyze()
