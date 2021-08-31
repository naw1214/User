class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    
guido = User('Guido', 'guido@gmail.com')
monty = User('Monty', 'monty@gmail.com')
micheal = User('Micheal', 'micheal@gmail.com')

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawl(50)
print(guido.account_balance)

monty.make_deposit(200)
monty.make_deposit(200)
monty.make_withdrawl(100)
monty.make_withdrawl(100)
print(monty.account_balance)

micheal.make_deposit(500)
micheal.make_withdrawl(120)
micheal.make_withdrawl(120)
micheal.make_withdrawl(120)
print(micheal.account_balance)