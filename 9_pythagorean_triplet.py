"""
Problem 9:
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
"""

from typing import Tuple

from math import prod

def pythagoras(a: int, b: int) -> float:
    """
    Computes pythagorean theorem (a² + b² = c²)

    Args:
        a (int): a
        b (int): b

    Returns:
        float: c
    """
    
    return (a**2 + b**2)**0.5

def find_triplet(sum_result: int) -> Tuple[int] | None:
    """
    Finds a pythagorean triplet with a given sum
    
    Args:
        sum_result (int): Desired sum of the triplet

    Returns:
        Tuple[int]: Tuple containing triplet
        None: If no triplet found
    
    """
    
    for a in range(1, sum_result // 2):
        for b in range(2, sum_result // 2):
            c = pythagoras(a, b)
            
            if a + b + c == sum_result:
                return (a, b, c)
            
    return None


def triplet_product(sum_result) -> int | None:
    """
    Finds the product of a pythagorean triplet with a given sum

    Args:
        sum_result (_type_): Sum of pythagorean triplet

    Returns:
        int: Product abc
        None: If no triplet found
    """
    
    triplet = find_triplet(sum_result=sum_result)
    
    return prod(triplet)
    
print(triplet_product(1000))