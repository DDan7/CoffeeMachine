# water, milk, coffee, cups, money = 400, 540, 120, 9, 550
#
#
# def buy():
#     global water
#     global milk
#     global coffee
#     global cups
#     global money
#     coffee_type = input("What do you want to buy? 1 - expresso, 2 - latte,\
# 3 - coppucinno, back - to the main menu:\n")
#     if coffee_type == 'back':
#         return
#     coffee_type_int = int(coffee_type)
#     if coffee_type_int == 1:
#         if water < 250:
#             print('Sorry, not enough water!')
#         elif coffee < 16:
#             print('Sorry, not enough coffee!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water = water-250
#             coffee = coffee-16
#             money = money+4
#             cups = cups-1
#     elif coffee_type_int == 2:
#         if water < 350:
#             print('Sorry, not enough water!')
#         elif milk < 75:
#             print('Sorry, not enough milk!')
#         elif coffee < 20:
#             print('Sorry, not enough coffee!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water = water-350
#             milk = milk-75
#             coffee = coffee-20
#             money = money+7
#             cups = cups-1
#     elif coffee_type_int == 3:
#         if water < 200:
#             print('Sorry, not enough water!')
#         elif milk < 100:
#             print('Sorry, not enough milk!')
#         elif coffee < 12:
#             print('Sorry, not enough coffee!')
#         else:
#             print('I have enough resources, making you a coffee!')
#             water = water-200
#             milk = milk-100
#             coffee = coffee-12
#             money = money+6
#             cups = cups-1
#
#
# def fill():
#     global water
#     global milk
#     global coffee
#     global cups
#     global money
#     water = water+int(input("Write how many ml of water do you want to add:\n"))
#     milk = milk+int(input("Write how many ml of milk do you want to add:\n"))
#     coffee = coffee+int(input("Write how many grams of coffee beans do you want to add:\n"))
#     cups = cups+int(input("Write how many disposable cups of coffee do you want to add:\n"))
#
#
# def take():
#     global money
#     print("I gave you ${}".format(money))
#     money = money-money
#
#
# def remaining():
#     print("""The coffee machine has:
# {} of water
# {} of milk
# {} of coffee beans
# {} of disposable cups
# ${} of money
# """.format(water, milk, coffee, cups, money))
#
#
# while True:
#     user_input = input("Write action (buy, fill, take, remaining, exit):\n")
#
#
#     def menu(user_input_):
#         if user_input_ == 'buy':
#             buy()
#         elif user_input_ == 'fill':
#             fill()
#         elif user_input_ == 'take':
#             take()
#         elif user_input_ == 'remaining':
#             remaining()
#
#
#     if user_input == 'exit':
#         break
#
#     menu(user_input)

class CoffeeMachine:

    # definition of the constructor class

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    # definition of the main function

    def main(self):
        while True:
            user_input_ = input("Write action (buy, fill, take, remaining, exit):\n")
            if user_input_ == 'buy':
                cofmac.buy()
            elif user_input_ == 'fill':
                cofmac.fill()
            elif user_input_ == 'take':
                cofmac.take()
            elif user_input_ == 'remaining':
                cofmac.remaining()
            elif user_input_ == 'exit':
                break

    # buy coffee

    def buy(self):
        coffee_type = input(
            "What do you want to buy? 1 - expresso, 2 - latte, 3 - coppucinno, back - to the main menu:\n")
        if coffee_type == 'back':
            return
        elif int(coffee_type) == 1:
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water = self.water-250
                self.coffee = self.coffee-16
                self.money = self.money+4
                self.cups = self.cups-1
        elif int(coffee_type) == 2:
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water = self.water-350
                self.milk = self.milk-75
                self.coffee = self.coffee-20
                self.money = self.money+7
                self.cups = self.cups-1
        elif int(coffee_type) == 3:
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.coffee < 12:
                print('Sorry, not enough coffee!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water = self.water-200
                self.milk = self.milk-100
                self.coffee = self.coffee-12
                self.money = self.money+6
                self.cups = self.cups-1

    # fill up the coffee machine

    def fill(self):
        self.water = self.water+int(input("Write how many ml of water do you want to add:\n"))
        self.milk = self.milk+int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee = self.coffee+int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups = self.cups+int(input("Write how many disposable cups of coffee do you want to add:\n"))

    # take money from the coffee machine

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money -= self.money

    # reveal the current status of the coffee machine

    def remaining(self):
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money
""".format(self.water, self.milk, self.coffee, self.cups, self.money))


if __name__ == '__main__':
    cofmac = CoffeeMachine(400, 540, 120, 9, 550)
    cofmac.main()
