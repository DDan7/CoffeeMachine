# put your python code here
a = int(input())
b = int(input())


result = []
for i in range(a, b + 1):
    if i % 3 == 0:
        result.append(i)
average = sum(result) / len(result)
print(average)
