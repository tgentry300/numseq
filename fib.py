'''Fibonacci function returns nth number in sequence'''


def fib(n):
    '''Fibonacci function returns nth number in sequence'''
    result = 0
    y = 0
    x = 1
    if n == 0:
        return 0

    elif n == 1:
        return 1

    for _ in range(n - 2):
        result = x + y
        y = x
        x = result

    return result
