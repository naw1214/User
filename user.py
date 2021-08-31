class User:		# here's what we have so far
    def __init__(self, name, email): # makes the instance of the class
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer(self,amount,user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


    
guido = User('Guido', 'guido@gmail.com')
monty = User('Monty', 'monty@gmail.com')
micheal = User('Micheal', 'micheal@gmail.com')

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

monty.make_deposit(200).make_deposit(200).make_withdrawl(100).make_withdrawl(100).display_user_balance()

micheal.make_deposit(500).make_withdrawl(120).make_withdrawl(120).make_withdrawl(120).display_user_balance()

guido.transfer(150, micheal)