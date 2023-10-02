from tqdm import tqdm
from time import perf_counter
import math
from typing import Dict

def generate_triplets(max_length: int) -> Dict[int, int]:
	combinations = {}
	
	
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
				combinations[s*k] = combinations.get((s*k), 0) + 1
				k += 1
    
	return combinations


def get_unique(max_length: int) -> int:
	combinations = generate_triplets(max_length=max_length)
	
	return len([s for s in combinations.values() if s == 1])

start = perf_counter()
print(get_unique(1500000))
end = perf_counter()
print(f"Elapsed: {round(end - start, 2)} s")

