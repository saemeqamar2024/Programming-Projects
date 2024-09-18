import math

# A class that finds the nearest square numbers to n.
class NearestSquareNumbers:

    def __init__(self, input):
        self.input = input

    # Finding the closest square number less than n.
    def find_closest_lower_square_number(self):
        n = self.input
        while n >= 2:
            if math.sqrt(n) in numbers_sequence_to_n(n):
                return n
            n -= 1
        return n

    # Finding the closest square number greater than n.
    def find_closest_higher_square_number(self, lower_square_root):
        higher_square_number = pow((lower_square_root+1),2)
        return higher_square_number

    # Finding the nearest square number to the input number.
    def nearest_square_number(self, lower_square_number, higher_square_number):
        if self.input - lower_square_number > higher_square_number - self.input:
            print(int(higher_square_number))
        else:
            print(int(lower_square_number))

# Creating a sequence of numbers from 1 to n.
def numbers_sequence_to_n(input_number):
    numbers_to_n = range(1, input_number + 1)
    return numbers_to_n

def nearest_sq(n):
    if n < 0 :
        print("Only positive integers accepted !")
    elif n == 0 :
        print(0)
    elif n == 1:
        print(1)
    else:
        if math.sqrt(n) in numbers_sequence_to_n(n):
            print(f'{n}')
        else:
            # Finding the square root of the closest lower square number.
            object1 = NearestSquareNumbers(n)
            lower_square_number = object1.find_closest_lower_square_number()
            lower_square_root = math.sqrt(lower_square_number)
            # Finding the closest higher square number.
            higher_square_number = object1.find_closest_higher_square_number(lower_square_root)
            # Finding the nearest square number to the input number.
            object1.nearest_square_number(lower_square_number, higher_square_number)


# nearest_sq(-1)
# nearest_sq(0)
# nearest_sq(1)
# nearest_sq(2)
# nearest_sq(10)
# nearest_sq(111)
nearest_sq(9999)
