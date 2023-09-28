"""
Problem 5:
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""


from typing import List, Dict
from time import perf_counter

def find_prime_factors(n: int) -> List[int]:
    """
    Find the prime factors a number n

    Args:
        n (int): Number for which to find prime factors

    Returns:
        List[int]: List containing all the prime factors
    """
    
     
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)
            
    if n > 1:
        factors.append(n)
        
    return factors


def simplify(factors: List[int]) -> Dict[str, int]:
    """
    Collects factors into dictionary, key - base, value - exponent

    Args:
        factors (List[int]): List containing individual prime factors (20 - [2, 2, 5])

    Returns:
        Dict[str, int]: Dictionary containing prime factors (20 - {2: 2, 5: 1})
    """
    simplified = {}
    
    for factor in factors:
        if factor not in simplified.keys():
            simplified[factor] = 1
        
        else:
            simplified[factor] += 1

    return simplified

def find_lcm(a: int, b: int) -> int:
    """
    Find lowest common multiple of all number between two numbers inclusive

    Args:
        a (int): min number (inclusive)
        b (int): max number (inclusive)

    Returns:
        int: LCM
    """
    prime_factors = [find_prime_factors(i) for i in range(a, b+1)]
    factors = [simplify(factors) for factors in prime_factors]
    largest_factors = {}
    lcm = 1
    
    for simplified_factors in factors:
        for base, exponent in simplified_factors.items():
            if base not in largest_factors:
                largest_factors[base] = exponent
            
            else:
                if exponent > largest_factors[base]:
                    largest_factors[base] = exponent
                    
    for base, exponent in largest_factors.items():
        lcm *= base**exponent
        
    return lcm
            
start = perf_counter()
print(find_lcm(2, 20))
end = perf_counter()

print(f"Elapsed: {round(((end - start) * 1000), 2)} ms.")

