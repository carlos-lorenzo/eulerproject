"""
Given that L is the length of the wire, for how many values of L <= 1,500,000 
can exactly one integer sided right angle triangle be formed?
"""


import math
from typing import Dict

def generate_triplets(max_length: int) -> Dict[int, int]:
	"""
	Finds all pythagorean triplets up until a given sum using eucledian equations
	
	Args:
		max_length (int): Max sum of the triplet

	Returns:
		Dict[int]: Dict containing triplet sum and its count {sum: count}
	
	"""
	combinations: Dict[int, int] = {}
	
	
	for m in range(2, int(math.sqrt(max_length))):
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
			while k*s <= max_length:
                # Generates non-primitive triplets
				combinations[s*k] = combinations.get((s*k), 0) + 1 # .get avoids if (s*k) in combinations
				k += 1
	
	return combinations


def get_unique(max_length: int) -> int:
	"""
	Gets the amount of unique pythagorean triplets (only one triplet with a given sum)

	Args:
		max_length (int): The maximum sum

	Returns:
		int: Number of unique triplets
	"""
	combinations = generate_triplets(max_length=max_length)
	
	return len([s for s in combinations.values() if s == 1])


print(get_unique(150000))

