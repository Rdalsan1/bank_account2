class BankAccount:
    title = "Raj's Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self._current_balance = current_balance  # Protected
        self._minimum_balance = minimum_balance  # Protected
        self.__account_number = account_number  # Private
        self.__routing_number = routing_number  # Private

    def deposit(self, amount):
        self._current_balance += amount
        print(f"{amount} deposited. New balance: {self._current_balance}")

    def withdraw(self, amount):
        if self._current_balance - amount < self._minimum_balance:
            print("Withdrawal denied. Insufficient funds.")
        else:
            self._current_balance -= amount
            print(f"{amount} withdrawn. New balance: {self._current_balance}")

    def print_customer_information(self):
        print(
            f"Bank: {BankAccount.title}\nCustomer: {self.customer_name}\nBalance: {self._current_balance}\nMinimum Balance: {self._minimum_balance}")

    def get_account_info(self):
        return f"Account Number: {self.__account_number}, Routing Number: {self.__routing_number}"
