class Account:
    def __init__(self, balance=0.0, interest_rate=0.0):
        self._balance = balance
        self._interest_rate = interest_rate
        self._interest_earned = 0.0

    def calculate_interest(self, months):
        """Calculates interest earned based on balance, interest rate, and months."""
        return self._balance * (self._interest_rate / 100) * (months / 12)

    def set_balance(self, new_balance):
        """Updates the account balance."""
        self._balance = new_balance

    def set_interest(self, interest_earned):
        """Updates the interest earned."""
        self._interest_earned = interest_earned

    def get_balance(self):
        """Returns the current balance."""
        return self._balance

    def get_interest_earned(self):
        """Returns the interest earned."""
        return self._interest_earned
