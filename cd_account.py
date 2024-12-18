from Account import Account

def create_cd_account(balance, interest_rate, months):
    # Create an instance of the Account class
    cd_account = Account(balance, interest_rate)
    
    # Calculate interest earned
    interest_earned = cd_account.calculate_interest(months)
    
    # Update the balance
    updated_balance = balance + interest_earned
    
    # Set the updated balance and interest earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    
    return updated_balance, interest_earned


