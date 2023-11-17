numbers_list = [int(x) for x in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)
