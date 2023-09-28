"""
Problem 3:
What is the largest prime factor of the number 600851475143?
"""
from typing import List
import math

def prime_factors(n: int) -> List[int]:
    """
    Find the prime factors a number n

    Args:
        n (int): Number for which to find prime factors

    Returns:
        List[int]: List containing all the prime factors
    """
    
    
    factors = []
    f = 2 #current factor
    while f < math.sqrt(n):
        while n % f == 0:
            n = n/f
            factors.append(f)
        f += 1
    factors.append(n)
    return factors


print(max(prime_factors(600851475143))) # Largest prime factor => max in list


