from bank_account import *  # Imports all classes and exceptions from bank_account.py

# Create a BankAccount object for Dave
Dave = BankAccount(1000, "Dave")  # initialAmount=1000, accountName="Dave"

# Create a BankAccount object for Sara
Sara = BankAccount(2000, "Sara")  # initialAmount=2000, accountName="Sara"

Dave.getBalance()  # Displays Dave's current balance
Sara.getBalance()  # Displays Sara's current balance

# call the method
Sara.deposit(500)  # Deposits $500 into Sara's account; amount=500

# calling Withdraw method here
Dave.withdraw(100000)  # Attempts to withdraw $100, which exceeds Dave's balance; should trigger BalanceException

# now go with 10 dollars 
Dave.withdraw(10)  # Withdraws $10 from Dave's account; amount=10

# transfer method
Dave.transfer(100, Sara)  # Transfers $100 from Dave to Sara; amount=100, account=Sara

# InterestRewardAcct
Jim = InterrestRewardAcct(1000, "Jim")  # Creates a special account for Jim with interest rewards; initialAmount=1000, accountName="Jim"

# get the balance
Jim.getBalance()  # Displays Jim's current balance

# deposit
Jim.deposit(100)  # Deposits $100 into Jim's account with 5% reward; amount=100

# transfer
Jim.transfer(100, Dave)  # Transfers $100 from Jim to Dave; amount=100, account=



