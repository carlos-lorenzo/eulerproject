import math

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


def replace_repeated_with_asterisk(n: int) -> str:
    digits_seen = set()
    result = []
    for digit in str(n):
        if digit in digits_seen:
            result.append('*')
        else:
            result.append(digit)
            digits_seen.add(digit)
    return ''.join(result)


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

def get_prime_family(formated_n: str, desired: int) -> int:
    primes = 1
    for i in range(10):
        
        if 10 - (i + 10) < desired - primes:
            return False
        
        if is_prime(int("".join([str(i) if char == "*" else char for char in formated_n]))):
            primes += 1
            
        
            
            
            
        
get_prime_family("1**0")

