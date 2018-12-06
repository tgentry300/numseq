'''find prime numbers'''


def is_prime(x):
    '''checks if x is prime'''
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


def primes(n):
    '''returns all prime numbers in range n'''
    new_list = []
    for num in range(n):
        if is_prime(num):
            new_list.append(num)
    return new_list
