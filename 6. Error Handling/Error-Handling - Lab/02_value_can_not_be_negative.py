class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f"{value} is negative")


def validate_positive_numbers(nums):
    for n in nums:
        if n < 0:
            raise ValueCannotBeNegativeError(n)


numbers = [1, 2, -3, 4, 5]

validate_positive_numbers(numbers)
print("Numbers are positive")
