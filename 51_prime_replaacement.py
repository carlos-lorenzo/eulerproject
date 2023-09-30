import math
from tqdm import tqdm
from typing import List


searched = set()
wildcards = []
primes = []

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



    digits_count = {}
    result = []
    
    for digit in str(n):
        if digit in digits_count:
            digits_count[digit] += 1
        else:
            digits_count[digit] = 1

    for digit in str(n):
        if digits_count[digit] > 1:
            result.append('*')
        else:
            result.append(digit)
    
    return ''.join(result)


# generate every possible wildcard strings
def generate_wildcards(s, index):
   
    if index > 0 and s not in searched:
        wildcards.append(s)
        searched.add(s)
    for x in range(index, len(s)):
        generate_wildcards(createPlaceholder(s, x), x+1)
    
    return wildcards
# replace a character with '*'
def createPlaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]

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

   

    
         
     
     
FAMILY = 8
   
for x in tqdm(range(12000, 130000)):
    found = False
    for i in range(0, len(primes)):
        if x % primes[i] == 0:
            found = True
            break
        if primes[i] * primes[i] > x:
            break
    if not found:
        primes.append(x)
                



for prime in primes:
    wildcards = []
    generate_wildcards(str(prime), 0)
    
    for match in wildcards:
        
        count = 0
        # fill up the asterisk with 0-9
        for z in range(0, 10):
            num = int(match.replace('*', str(z)))
            if len(str(num)) < len(match):
                continue
            if is_prime(num):
                count += 1
        # if counter is at least 8 then print and exit program
        if count >= 8:
            print(prime)
            print(match)
            exit(0)

            