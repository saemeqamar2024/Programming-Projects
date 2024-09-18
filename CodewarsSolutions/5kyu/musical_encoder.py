decoded_list = [] # Stores the output list.
consecutive_numbers = [] # Stores three or more consecutive numbers in a sequence.
interval_numbers = [] # Stores three or more numbers with the same difference in intervals in a sequence (> 1, < -1).
repeated_numbers = [] # Stores a list of two or more identical numbers.

def two_identical_numbers(first_number, second_number):
    repeated_numbers.append(first_number)
    repeated_numbers.append(second_number)

    return repeated_numbers

def three_identical_numbers(first_number, second_number, third_number):
    repeated_numbers.append(first_number)
    repeated_numbers.append(second_number)
    repeated_numbers.append(third_number)

    return repeated_numbers

# Adding more numbers to the interval numbers sequence when there are three
# numbers with the same interval value of greater than 1 or less than -1.
def interval_between_three_numbers(first_number, second_number, third_number):

    interval_numbers.append(first_number)
    interval_numbers.append(second_number)
    interval_numbers.append(third_number)

    return interval_numbers

#  Adding more numbers to the consecutive numbers sequence
#  when there are two consecutive numbers remaining in the current sequence.
def two_consecutive_numbers(first_number_to_add, second_number_to_add):
    consecutive_numbers.append(first_number_to_add)
    consecutive_numbers.append(second_number_to_add)

    return consecutive_numbers

#  Adding more numbers to the consecutive numbers sequence
#  with three consecutive numbers.
def three_consecutive_numbers(input_array, first_number, second_number, third_number):
  if third_number == input_array[-1]:
    consecutive_numbers.append(first_number)
    consecutive_numbers.append(second_number)
    consecutive_numbers.append(third_number)
  else:
    consecutive_numbers.append(first_number)

  return consecutive_numbers

# The processing of the input array into a decoded list is based upon the following:
# the length of the list, the differences between numbers next to one another.
def compress(raw):

    # The first, second and third numbers' indexes in the input array.
    first_number_index = 0
    second_number_index = 1
    third_number_index = 2

    if len(raw) == 1:
        decoded_list.append(raw[first_number_index])
    elif len(raw) == 2:
        if raw[first_number_index] == raw[second_number_index]:
            repeated_numbers_sequence = two_identical_numbers(raw[first_number_index], raw[second_number_index])
            repeating_nums = f'{raw[first_number_index]}*{len(repeated_numbers_sequence)}'
            decoded_list.append(repeating_nums)
            repeated_numbers.clear()
        else:
            decoded_list.append(raw[first_number_index])
            decoded_list.append(raw[second_number_index])
    elif len(raw) >= 3:
        for x in raw[first_number_index : ]:
            # Case for when there are only two numbers remaining.
            if len(raw[first_number_index : ]) == 2:
                if raw[first_number_index] == raw[second_number_index]:
                    repeated_numbers_sequence = two_identical_numbers(raw[first_number_index], raw[second_number_index])
                    repeating_nums = f'{raw[first_number_index]}*{len(repeated_numbers_sequence)}'
                    decoded_list.append(repeating_nums)
                    repeated_numbers.clear()
                    break
                else:
                    decoded_list.append(raw[first_number_index])
                    decoded_list.append(raw[second_number_index])
                    break
            # Cases when there are three consecutive numbers, three numbers with same interval between them and three identical numbers.
            elif(raw[second_number_index] - raw[first_number_index]) == (raw[third_number_index] - raw[second_number_index]):
                # Dealing with three or more ascending or descending consecutive numbers.
                if ((x + 1 == raw[second_number_index]) & (raw[second_number_index] + 1 == raw[third_number_index]) |
                    ((x - 1 == raw[second_number_index]) & (raw[second_number_index] - 1 == raw[third_number_index]))):
                    consecutive_nums_sequence = three_consecutive_numbers(raw[third_number_index : ], raw[first_number_index], raw[second_number_index], raw[third_number_index])
                    if len(raw[third_number_index : ]) == 1 :
                        consecutive_nums = f'{consecutive_nums_sequence[0]}-{consecutive_nums_sequence[-1]}'
                        decoded_list.append(consecutive_nums)
                        consecutive_numbers.clear()
                        break
                    else:
                        first_number_index += 1
                        second_number_index += 1
                        third_number_index += 1
                # Dealing with three or more numbers next to each other that have the same interval (>1 or <-1).
                elif (((raw[second_number_index] - x) > 1) & ((raw[third_number_index] - raw[second_number_index]) > 1) |
                      ((raw[second_number_index] - x) < -1) & ((raw[third_number_index] - raw[second_number_index]) < -1)):
                        if len(raw[third_number_index : ]) == 1:
                            interval_numbers_sequence = interval_between_three_numbers(x, raw[second_number_index], raw[third_number_index])
                            interval_nums = f'{interval_numbers_sequence[0]}-{interval_numbers_sequence[-1]}/{raw[third_number_index] - raw[second_number_index]}'
                            decoded_list.append(interval_nums)
                            interval_numbers.clear()
                            break
                        # First, second and third numbers have same intervals, but third and fourth numbers have different intervals
                        elif len(raw[third_number_index : ]) >= 2:
                            if raw[third_number_index + 1] - raw[third_number_index] != raw[third_number_index] - raw[second_number_index]:
                                interval_numbers_sequence = interval_between_three_numbers(x, raw[second_number_index], raw[third_number_index])
                                interval_nums = f'{interval_numbers_sequence[0]}-{interval_numbers_sequence[-1]}/{raw[third_number_index] - raw[second_number_index]}'
                                decoded_list.append(interval_nums)
                                if len(raw[third_number_index : ]) == 2:
                                    decoded_list.append(raw[third_number_index + 1])
                                    interval_numbers.clear()
                                    break
                                elif len(raw[third_number_index : ]) == 3:
                                    decoded_list.append(raw[third_number_index + 1])
                                    decoded_list.append(raw[third_number_index + 2])
                                    interval_numbers.clear()
                                    break
                                elif len(raw[third_number_index : ]) > 3:
                                    first_number_index += 3
                                    second_number_index += 3
                                    third_number_index += 3
                            else:
                                interval_numbers.append(x)
                                first_number_index += 1
                                second_number_index += 1
                                third_number_index += 1
                # Dealing with three or more identical numbers.
                elif (x == raw[second_number_index]) & (raw[second_number_index] == raw[third_number_index]):
                    if len(raw[third_number_index : ]) == 1:
                        repeated_numbers_sequence = three_identical_numbers(x, raw[second_number_index], raw[third_number_index])
                        repeating_nums = f'{raw[second_number_index]}*{len(repeated_numbers_sequence)}'
                        decoded_list.append(repeating_nums)
                        repeated_numbers.clear()
                        break
                    else:
                        repeated_numbers.append(x)
                        first_number_index += 1
                        second_number_index += 1
                        third_number_index += 1
            else:
                # Case when only the first number and second number are consecutive (and the third is not).
                # First number cannot be the first number at the start of the input array.
                if((x + 1 == raw[second_number_index]) & (raw[second_number_index] + 1 != raw[third_number_index]) |
                (x - 1 == raw[second_number_index]) & (raw[second_number_index] - 1 != raw[third_number_index])):
                    if x != raw[0]:
                        consecutive_nums_sequence = two_consecutive_numbers(x, raw[second_number_index])
                        consecutive_nums = f'{consecutive_nums_sequence[0]}-{consecutive_nums_sequence[-1]}'
                        decoded_list.append(consecutive_nums)
                        consecutive_numbers.clear()
                        if len(raw[third_number_index : ]) == 1:
                            decoded_list.append(raw[third_number_index])
                            break
                        elif len(raw[third_number_index : ]) == 2:
                            first_number_index += 2
                            second_number_index += 2
                        elif len(raw[third_number_index : ]) >= 3:
                            first_number_index += 2
                            second_number_index += 2
                            third_number_index += 2
                # Case when first and second numbers and identical (and third number is not).
                elif x == raw[second_number_index] & raw[second_number_index] != raw[third_number_index]:
                    repeated_numbers_sequence = two_identical_numbers(x, raw[second_number_index])
                    repeating_nums = f'{raw[second_number_index]}*{len(repeated_numbers_sequence)}'
                    decoded_list.append(repeating_nums)
                    repeated_numbers.clear()
                    if len(raw[third_number_index : ]) == 1:
                        decoded_list.append(raw[third_number_index])
                        break
                    elif len(raw[third_number_index :]) == 2:
                        decoded_list.append(raw[third_number_index])
                        decoded_list.append(raw[third_number_index + 1])
                        break
                    elif len(raw[third_number_index: ]) >= 3:
                        first_number_index += 2
                        second_number_index += 2
                        third_number_index += 2
                else:
                    decoded_list.append(raw[first_number_index])
                    first_number_index += 1
                    second_number_index += 1
                    third_number_index += 1

    interval_numbers.clear()
    repeated_numbers.clear()
    consecutive_numbers.clear()

    print(decoded_list)
    decoded_list.clear()


compress([1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
compress([0, 2, 4, 5, 7, 8, 9])
compress([0, 2, 4, 5, 7, 6, 5])
compress([0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5])
compress([1, 2, 2, 3])
compress([1, 3, 4, 5, 7])
compress([1, 10, 8, 6, 7])