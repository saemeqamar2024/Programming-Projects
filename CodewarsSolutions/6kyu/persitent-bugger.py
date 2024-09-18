# Write a function, persistence, that takes in a positive parameter num
# and returns its multiplicative persistence, which is the number of times
# you must multiply the digits in num until you reach a single digit.

# Multiplying the digits of a number with more than one digit.
def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)

    return result


def persistence(n):
    steps = 0
    while len(str(n)) != 1:
        result = multiply_digits(n)
        n = result
        steps += 1

    return steps


print(persistence(3))
print(persistence(39))
print(persistence(25))
print(persistence(999))