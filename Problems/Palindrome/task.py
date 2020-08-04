user_input = input()


def palindrome(a):
    backward = a[::-1]
    if backward == a:
        print("Palindrome")
    else:
        print("Not palindrome")


palindrome(user_input)


# def palindrome(a):
#     backward = ''
#     for i in a:
#         backward += i
#     if backward == a:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
#
#
# palindrome(user_input)
