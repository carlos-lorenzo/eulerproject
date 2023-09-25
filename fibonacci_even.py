"""
Problem 2:

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

import math


def fibonacci(n: int) -> int:
    """
    nth term for fibonacci sequence
    
    source: https://en.wikipedia.org/wiki/Fibonacci_sequence

    Args:
        n (int): position of item in sequence

    Returns:
        int: Number in sequence of position n
    """
    
    
    PHI = (1 + math.sqrt(5)) / 2
    PSI = 1 - PHI
    
    return round((PHI**n - PSI**n) / ((2 * PHI) - 1))



sum_terms = 0
n = 1
while True:
    term = fibonacci(n=n)
    
    if term > 4000000:
        break
    
    if term % 2 == 0:
        sum_terms += term
        
    n += 1
    
print(sum_terms)



