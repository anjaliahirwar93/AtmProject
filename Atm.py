class ATM:
    def __init__(self):
        """
        Initialize the ATM with a starting balance of 0, a default PIN, and an empty transaction history.
        """
        self.balance = 0
        self.pin = "1234"
        self.transaction_history = []

    def check_balance(self):
        """
        Return the current account balance.
        """
        return self.balance

    def deposit_cash(self, amount):
        """
        Deposit a specified amount into the account.
        
        Args:
        amount (float): The amount to be deposited.
        
        Returns:
        str: A message indicating the success or failure of the deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"${amount} deposited successfully. Current balance: ${self.balance}"
        return "Invalid deposit amount."

    def withdraw_cash(self, amount):
        """
        Withdraw a specified amount from the account if the balance is sufficient.
        
        Args:
        amount (float): The amount to be withdrawn.
        
        Returns:
        str: A message indicating the success or failure of the withdrawal.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"${amount} withdrawn successfully. Current balance: ${self.balance}"
        return "Invalid withdrawal amount or insufficient balance."

    def change_pin(self, old_pin, new_pin):
        """
        Change the PIN if the old PIN is correct.
        
        Args:
        old_pin (str): The current PIN.
        new_pin (str): The new PIN to be set.
        
        Returns:
        str: A message indicating the success or failure of the PIN change.
        """
        if old_pin == self.pin:
            self.pin = new_pin
            self.transaction_history.append("PIN changed successfully.")
            return "PIN changed successfully."
        return "Incorrect old PIN."

    def get_transaction_history(self):
        """
        Return the transaction history as a list of strings.
        """
        return self.transaction_history

# Simulating ATM interaction
def atm_simulation():
    """
        Simulate the ATM interaction with a text-based menu for the user.
        """
    atm = ATM()

    while True:
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit_cash(amount))
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw_cash(amount))
        elif choice == '4':
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(old_pin, new_pin))
        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.get_transaction_history():
                print(transaction)
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the simulation
if __name__ == "__main__":
    atm_simulation()
