"""
Problem 5:
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

import math
from typing import List, Dict

    
def find_prime_factors(n: int) -> List[int]:
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


def simplify(factors: List[int]) -> Dict[str, int]:
    simplified = {}
    
    for factor in factors:
        if factor not in simplified.keys():
            simplified[factor] = 1
        
        else:
            simplified[factor] += 1

    return simplified

def find_lcm(a, b) -> int:

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
            
    
print(find_lcm(2, 20)) # 1 not necessary

