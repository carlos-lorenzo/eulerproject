"""
Problem 5:
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""
from functools import lru_cache


@lru_cache(maxsize = 128)
def is_divisible(n: int, a: int, b: int) -> bool:
    """
    Checks if a number (n) is divisible (has no remainder) by all numbers from a to b

    Args:
        n (int): Number to be divided
        a (int): Smallest number to be checked (inclusive)
        b (int): Largest number to be checked (inclusive)

    Returns:
        bool: Weather or not the number is evenly divisible
    """
    
    
    for i in range(a, (b+1)):
       if n % i != 0:
            return False
    
    return True


@lru_cache(maxsize = 128)
def find_smallest_divisble(a: int, b: int) -> int:
    """
    Finds the smallest number that can be divided evenly (no remainder) by all numbers from a to b

    Args:
        a (int): Smallest number to be checked (inclusive)
        b (int): Largest number to be checked (inclusive)

    Returns:
        int: The smallest number found
    """
    
    n = b
    while True:
        if is_divisible(n, a, b):
            break
        
        n += 1
        
    return n



print(find_smallest_divisble(2, 20)) # 1 not necessary

