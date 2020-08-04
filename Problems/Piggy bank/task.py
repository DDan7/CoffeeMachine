class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.dollars += (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100


# bank = PiggyBank(1, 1)
# bank.add_money(0, 99)
# print(bank.dollars, bank.cents)
