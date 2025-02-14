from bank_account2.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, withdrawal_interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.withdrawal_interest_rate = withdrawal_interest_rate  # Public (e.g., 0.02 for 2% interest on each withdrawal)

    def withdraw(self, amount):
        interest = amount * self.withdrawal_interest_rate
        total_amount = amount + interest
        if self._current_balance - total_amount < self._minimum_balance:
            print(f"Withdrawal denied. Insufficient funds after adding {interest} interest.")
        else:
            self._current_balance -= total_amount
            print(f"{amount} withdrawn with {interest} interest deducted. New balance: {self._current_balance}")
