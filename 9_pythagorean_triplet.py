"""
Problem 9:
There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
"""

from typing import Tuple
import math


def find_triplet(perimeter: int) -> Tuple[int] | None:
	"""
	Finds a pythagorean triplet with a given sum
	
	Args:
		perimeter (int): Desired sum of the triplet

	Returns:
		Tuple[int]: Tuple containing triplet
		None: If no triplet found
	
	"""
	
	
	
	for m in range(2, int(math.sqrt(perimeter))):
		for n in range(1, m):
			
			if (m + n) % 2 != 1:
				continue
			
			if math.gcd(m, n) != 1:
				continue
			
			
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			s = a + b + c
			
			k = 1
			while k*s <= perimeter:
				if k*s == perimeter:
					return (k*a, k*b, k*c)
				k += 1
	
	return None


def triplet_product(sum_result: int) -> int | None:
	"""
	Finds the product of a pythagorean triplet with a given sum

	Args:
		sum_result (int): Sum of pythagorean triplet

	Returns:
		int: Product abc
		None: If no triplet found
	"""
	
	triplet = find_triplet(perimeter=sum_result)
	
	return math.prod(triplet)

print(triplet_product(1000))

