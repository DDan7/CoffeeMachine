class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area of the triangle
        self.area = (1 / 2) * (leg_1 * leg_2)


# take triangle input from user as str and transform it into int
input_c, input_a, input_b = [int(x) for x in input().split()]

# create an instance of "RightTriangle"
rtriangle = RightTriangle(input_c, input_a, input_b)

# check if Pythagorean theorem holds
if input_c ** 2 == input_a ** 2+input_b ** 2:
    print(rtriangle.area)
else:
    print('Not right')
