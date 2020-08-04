scores = input().split()


def test_game(a):
    correct, incorrect = 0, 0
    for i in a:
        if i == 'I':
            incorrect += 1
            if incorrect == 3:
                break
        elif i == 'C':
            correct += 1
    if incorrect == 3:
        print(f"""Game over
{correct}""")
    elif incorrect < 3:
        print((f"""You won
{correct}"""))


test_game(scores)


# Used for list that contains only one string
# for loop inside of the for loop

# scores = input().split()
#
# incorrect = 0
# correct = 0
# for l in range(len(scores)): # for l in scores: #probably it works like this also
#     for i in scores[l]:
#         if i == 'I':
#             incorrect += 1
#             if incorrect == 3:
#                 break
#         elif i == 'C':
#             correct += 1
# if incorrect == 3:
#     print(f"""Game over
# {correct}""")
# elif incorrect < 3:
#     print((f"""You won
# {correct}"""))