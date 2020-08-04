random_input = input().lower()

random_input2 = random_input\
    .replace(",", "")\
    .replace(".", "")\
    .replace("!", "")\
    .replace("?", "")

print(random_input2.lower())