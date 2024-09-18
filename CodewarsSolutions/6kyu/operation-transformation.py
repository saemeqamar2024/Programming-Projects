def operation(a, b):
    steps = 0
    while a != b:
        if a > b:
            if a % 2 != 0:
                a = (a - 1) / 2
            else:
                a /= 2
        elif a < b:
            a *= 2
        steps += 1

    return steps