from savings_account import SavingsAccount
from bank_account2.checking_account import CheckingAccount


def main():
    print("Welcome to Raj's Bank!")

    # Create sample accounts for demonstration
    savings1 = SavingsAccount("Raj Dalsaniya", 5000000, 2000000, "548291190", "987654321", 0.05)
    checking1 = CheckingAccount("Raj Dalsaniya", 2500000, 300000, "998877665", "667788990", 1000)

    accounts = {
        "savings": savings1,
        "checking": checking1
    }

    while True:
        print("\nWhat would you like to do?")
        print("1. View account information")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money (Checking Account only)")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        try:
            if choice == "1":
                account_type = input("Which account? (savings/checking): ").lower()
                if account_type in accounts:
                    accounts[account_type].print_customer_information()
                else:
                    print("Invalid account type. Please choose savings or checking.")

            elif choice == "2":
                account_type = input("Which account? (savings/checking): ").lower()
                if account_type in accounts:
                    amount = float(input("Enter the amount to deposit: "))
                    accounts[account_type].deposit(amount)
                else:
                    print("Invalid account type. Please choose savings or checking.")

            elif choice == "3":
                account_type = input("Which account? (savings/checking): ").lower()
                if account_type in accounts:
                    amount = float(input("Enter the amount to withdraw: "))
                    accounts[account_type].withdraw(amount)
                else:
                    print("Invalid account type. Please choose savings or checking.")

            elif choice == "4":
                if isinstance(accounts["checking"], CheckingAccount):
                    amount = float(input("Enter the amount to transfer: "))
                    accounts["checking"].transfer(amount)
                else:
                    print("This action is only available for Checking Account.")

            elif choice == "5":
                print("Thank you for banking with us. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()