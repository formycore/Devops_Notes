class BankAccount:
	def __init__(self,initialAmount,accountName):
		self.balance = initialAmount
		self.name = accountName
		print(f"\nAccount '{self.name}' created.\nBalance='{self.balance:.2f}'")

	# add another method
	def getBalance(self):
		# it gets only the balance of the account
		print(f"\nAccount '{self.name}' balance=$'{self.balance:.2f}'")
	# call this from oop_project file
        
