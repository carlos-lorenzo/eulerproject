"""
Problem 10:
Find the sum of all the primes below two million.
"""


from math import sqrt

def is_prime(n: int) -> bool:
    """
    Checks weather a number is prime or not

    Args:
        n (int): Number to be checked

    Returns:
        bool: Is prime? True/False
    """
    
    for factor in range(2, int(sqrt(n)+1)):
        if n % factor == 0:
            return False
        
    return True


def find_prime_sum(high: int) -> int:
    """
    Find the sum of all primes below a threshold

    Args:
        high (int): Max number

    Returns:
        int: Sum of primee
    """
    
    prime_sum = 0

    for i in range(2, high):
        if is_prime(i):
            prime_sum += i

    return prime_sum


print(find_prime_sum(high=2000000))