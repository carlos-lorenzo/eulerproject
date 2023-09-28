"""
Problem 7:
What is the 10001st prime number?
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




def find_nth_prime(n: int) -> int:
    """
    Finds nth prime. 
    
    First six prime numbers: 2, 3, 5, 7, 11, 13
    ==> if n = 3, nth prime = 5

    Args:
        n (int): Index of number (starting from 1)

    Returns:
        int: Nth prime
    """
    
    n_found = 1
    current_num = 2
    
    while n_found != n:
        current_num += 1
        if is_prime(current_num):
            
            n_found += 1
         
        
        
    return current_num


print(find_nth_prime(n=10001))
