# Custom exception for handling insufficient balance scenarios
class BalanceException(Exception):
    pass  # No additional functionality, just a custom exception

# Main class representing a bank account
class BankAccount:
    # Constructor to initialize account with starting balance and name
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount  # Stores the current balance of the account
        self.name = accountName       # Stores the name of the account holder
        print(f"\nAccount '{self.name}' created.\nBalance='{self.balance:.2f}'")  # Confirmation message

    # add another method
    # Method to display the current balance of the account
    def getBalance(self):
        # it gets only the balance of the account
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")  # Prints the balance

    # call this from oop_project file
    # add another method
    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance = self.balance + amount  # Adds the deposit amount to the balance
        #print(f"\n Deposit Complete \nAccount '{self.name}' balance=${self.balance:.2f}")
        print("\n Deposit Complete")          # Confirmation message
        self.getBalance()                     # Shows updated balance

    # this is withdraw method
    # whenever we do a withdraw we need to check if we have enough funds or not to complete the transaction
    # Method to check if a transaction is possible with the given amount
    def viableTransaction(self, amount):
        # amount: the value to check against the current balance
        if self.balance >= amount:            # Checks if balance is sufficient
            return # if the desired amount is less or equal to deposit there is no issue
        else:
            # Raises exception if balance is insufficient
            raise BalanceException(
                f"\n Sorry account '{self.name}' has only a balance of $'{self.balance:.2f}'"
            )

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # amount: the value to withdraw from the account
        try:
            self.viableTransaction(amount)    # Checks if withdrawal is possible
            self.balance = self.balance - amount  # Deducts the amount from balance
            print("\n Withdraw complete")         # Confirmation message
            self.getBalance()                    # Shows updated balance
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")  # Prints error if insufficient funds

    # Method to transfer money from this account to another account
    def transfer(self, amount, account): # account here is for second account 
        # amount: the value to transfer
        # account: the BankAccount object to receive the transfer
        try:
            print("\n**********\n\n Begining the new transaction. ")  # Transaction start message
            self.viableTransaction(amount)    # Checks if transfer is possible
            self.withdraw(amount)             # Withdraws from this account
            account.deposit(amount)           # Deposits into the target account
            print("\nTransfer Complete!\n\n*********")  # Confirmation message
        except BalanceException as error:
            print(f"Transfer Interrupted: {error}")     # Prints error if insufficient funds

# Subclass representing a special account with interest rewards on deposits
class InterrestRewardAcct(BankAccount):
    # BankAccount is the parent we are going to inherit from 
    # there are no new properties no need for inializer at the top init function
    # overwrite the deposit method
    # any deposit in this account will get added five percent to the amount that's going in as the deposit that's the reward
    # Method to deposit money with a 5% reward
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)  # Adds deposit plus 5% reward
        print("\n Deposit complete.")                   # Confirmation message
        self.getBalance()                              # Shows updated balance







