# Build a function that returns an array of integers from n to 1 where n>0.

def reverse_seq(n):
    if n > 0:
        one_to_n = list(range(1,n+1))
        print(one_to_n.reverse())
    else:
        print(0)

reverse_seq(5)