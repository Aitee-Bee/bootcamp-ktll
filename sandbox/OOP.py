class Account:
    
    def __init__(self, name, bank, card_type, account):
        self.name = name
        self.bank = bank
        self.card_type = card_type
        self.account = account
        self.limit = 100
        self.balance = 0

    def get_customer_name(self):
        return f"Customer's Name: {self.name}"

    def get_bank(self):
        return f"Bank Name: {self.bank}"   
    
    def make_payment(self, amount):
        self.balance += amount
        return f"{self.name} deposited #{amount}"

    def charge(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return f"{self.name} withdrew #{amount}. Current balance: {self.balance}"
        else:
            return "Insufficent funds"
     
# your class is just a template. you need to create an object and interact with them


account1 = Account("Buhari", "access_bank", "master", 23231)
account2 = Account("Tinubu", "polaris_bank", "verve", 8372892)

print(account1.get_customer_name())
print(account1.get_bank())
print(account1.make_payment(15000))
print(account1.charge(5000))
