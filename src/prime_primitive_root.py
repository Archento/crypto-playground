"""Python program to find primitive root of a given number n
"""
from math import sqrt


def is_prime(num=0):
    """Function to determine if the input number is a prime

    Args:
        num (int): input number

    Returns:
        bool: True if num is prime, False if not
    """
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def calculate_power(x = 0, y = 0, p = 0) -> int:
    """Iterative Function to calculate r^((phi)/primefactor) % number

    Args:
        x (int): equivalent to base
        y (int): equivalent of phi/primefactor
        p (int): equivalent of number

    Returns:
        int: _description_
    """
    res = 1  # Initialize result

    # update x if x >= p
    x = x % p

    while y > 0:
        # If y is odd, multiply x with result
        if y & 1:
            res = (res * x) % p

        # y will be even now
        y = y >> 1  # shift right -> y = y/2
        x = (x * x) % p

    return res


def find_prime_factors(num) -> set:
    """Function to store prime factors of a number

    Args:
        num (int): input number

    Returns:
        set: unique array of prime factors
    """
    prime_factors = set()

    # add 2 to the set if dividable by 2
    while num % 2 == 0:
        prime_factors.add(2)
        num = num // 2

    # the number will be odd at this point. So we can skip one element
    # NOTE: i = i + 2
    for i in range(3, int(sqrt(num)), 2):
        # while i divides num, add i to the set and divide num
        while num % i == 0:
            prime_factors.add(i)
            num = num // i

    # this condition is to handle the case when
    # the input number is a prime number greater than 2
    if num > 2:
        prime_factors.add(num)

    return prime_factors


def find_primitive(num) -> int:
    """Function to find the smallest primitive root of a given number

    Args:
        num (int): number to find primitive for

    Returns:
        int: primitive root, -1 if num is no prime
    """
    # Check if n is prime
    if is_prime(num) is False:
        return -1

    # Find value of Euler Totient function of n.
    # Since n is a prime number, the value of the Euler Totient function
    # is n-1 as there are n-1 relative prime numbers.
    phi = num - 1

    # Find prime factors of phi and store in a set
    prime_factors = find_prime_factors(phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi
        # and check if there is a phi with a power of 1
        flag = False
        for current in prime_factors:
            # Check if r^((phi)/primefactor) % number is 1
            if calculate_power(r, phi // current, num) == 1:
                flag = True
                break

        # If there was no power with value 1.
        if flag is False:
            return r

    # no primitive root found
    return -1
