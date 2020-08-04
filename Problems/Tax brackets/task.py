income = int(input())

tax = {132407: 28, 42708: 25, 15528: 15, 0: 0}

for tax_bracket, percent in tax.items():
    if income > tax_bracket:
        calculated_tax = round(income * percent / 100)
        print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
        break


# percent = [0, 15, 25, 28]
# tax_bracket = [15527, 42707, 132406, 9999999]
#
# for i in range(len(percent)):
#     if income < tax_bracket[i]:
#         calculated_tax = round(income * percent[i] / 100)
#         print(f'The tax for {income} is {percent[i]}%. That is {calculated_tax} dollars!')
#         break
