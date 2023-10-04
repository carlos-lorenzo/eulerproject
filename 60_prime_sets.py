"""
Problem 60:
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import math
from tqdm import tqdm

def sieve_eratosthenes(n: int) -> int:
    """
    Use the Sieve of Eratosthenes to find the nth prime number.
    
    Args:
        n (int): The position of the prime number to find (1 for the first prime, 2 for the second, and so on).
    
    Returns:
        int: The nth prime number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2  # The first prime
    elif n == 2:
        return 3  # The second prime
    elif n == 3:
        return 5  # The third prime
    elif n == 4:
        return 7  # The fourth prime
    elif n == 5:
        return 11  # The fifth prime

    limit = n * math.log(n * math.log(n))  # Adjusted limit based on n
    
    sieve = [True] * (int(limit) + 1)
    sieve[0] = sieve[1] = False
    count = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, int(limit) + 1, p):
                sieve[i] = False
    for p in range(2, int(limit) + 1):
        if sieve[p]:
            count += 1
            if count == n:
                return p


def is_prime(n: int) -> bool:
    """
    Checks weather a number is prime or not

    Args:
        n (int): Number to be checked

    Returns:
        bool: Is prime? True/False
    """
    
    for factor in range(2, int(math.sqrt(n)+1)):
        if n % factor == 0:
            return False
        
    return True

def find_arrangements(primes: list[int]) -> list[int]:
    arrangements = []
    
    for root in primes:
        for particle in primes:
            if root == particle:
                continue
            
            
            prefixed = int(f"{root}{particle}")
            sufixed = int(f"{particle}{root}")
            
            if prefixed not in arrangements:
                arrangements.append(prefixed)
                
            if sufixed not in arrangements:
                arrangements.append(sufixed)
            
    return arrangements


def is_all_prime(arrangements: list[int]) -> bool:
    for num in arrangements:
        if not is_prime(num):
            return False
    
    return True
    
    
MAX_PRIME = 10000
primes = []

for i in range(2, MAX_PRIME):
    prime = sieve_eratosthenes(i)
    if prime <= MAX_PRIME:
        primes.append(prime)
    else:
        break
    
primes.pop(primes.index(5)) # If 5 is last digit, num can't be prime


a = 3
b = 7
c = 109

for d in primes:
    for e in primes:
        nums = [a, b, c, d, e]
        if len(set(nums)) == 5 and is_all_prime(find_arrangements(nums)):
                print(a, b, c, d, e)   
                            
                    


