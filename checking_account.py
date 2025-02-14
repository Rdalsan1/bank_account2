from bank_account2.bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit  # Public

    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Transfer denied. Amount exceeds the transfer limit of {self.transfer_limit}.")
        elif self._current_balance - amount < self._minimum_balance:
            print("Transfer denied. Insufficient funds.")
        else:
            self._current_balance -= amount
            print(f"{amount} transferred. New balance: {self._current_balance}")
