class Account:
	def __init__(self,first_name,last_name,balance):
		self.first_name = first_name
		self.last_name = last_name
		self.balance = balance

	def welcome(self):
		return "Hello {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


	def deposit(self,y):
		deposit = y
		self.balance = self.balance + y

		dps = "Dear {} {} deposit of kes {} was successful current balance is {}".format(self.first_name,self.last_name,y,self.balance)
		return dps
		

	def withdraw(self,x):
		withdraw = x
		x<self.balance
		self.balance = self.balance - x

		msg = "Dear {} {} withdrawal of kes {} was successful current balance is {}".format(self.first_name,self.last_name,x,self.balance)
		return msg

	

	def show_balance(self):
		show_balance = self.balance
		text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
		return text