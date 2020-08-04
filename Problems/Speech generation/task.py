digits = ["zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine"]

phone_number = input()

for i in str(phone_number):
    print(digits[int(i)])