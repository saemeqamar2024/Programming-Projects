def divisors(integer):

    divisors_list = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors_list.append(i)

    if len(divisors_list) > 0:
        return f'{divisors_list}, integer = {integer}'
    else:
        return f'{integer} is prime, integer = {integer}'