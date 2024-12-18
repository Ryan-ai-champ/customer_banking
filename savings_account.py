from Account import Account

def create_savings_account(balance, interest_rate, months):
    # Create an instance of the Account class
    savings_account = Account(balance, interest_rate)
    
    # Calculate interest earned
    interest_earned = savings_account.calculate_interest(months)
    
    # Update the balance
    updated_balance = balance + interest_earned
    
    # Set the updated balance and interest earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    
    return updated_balance, interest_earned

