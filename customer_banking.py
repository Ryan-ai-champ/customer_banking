from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    print("Customer Banking System: Savings and CD Account Interest Calculator\n")
    
    # Savings Account
    print("---- Savings Account ----")
    savings_balance = float(input("Enter the starting balance for your Savings Account: $"))
    savings_interest_rate = float(input("Enter the annual interest rate (in %): "))
    savings_months = int(input("Enter the number of months: "))

    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )

    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}\n")

    # CD Account
    print("---- CD Account ----")
    cd_balance = float(input("Enter the starting balance for your CD Account: $"))
    cd_interest_rate = float(input("Enter the annual interest rate (in %): "))
    cd_months = int(input("Enter the number of months: "))

    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest_rate, cd_months
    )

    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}\n")

if __name__ == "__main__":
    main()
