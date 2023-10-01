from tqdm import tqdm
from time import perf_counter

def triplets_of_sum(n: int) -> int:
    triplets = set()
    
    for a in range(1, n // 3 + 1):
        # Calculate value of b
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
 
        # The value of c = n - a - b
        c = n - a - b
        
        if a * a + b * b == c * c and b > 0 and c > 0:
            triplet = tuple(sorted([a, b, c]))
            if triplet not in triplets:
                if len(triplets) == 1:
                    return 2
                
                triplets.add(triplet)
            
    return len(triplets)

def count_triangles(start, end):
    num_triangles = 0
    for l in range(start, end):
        if triplets_of_sum(l) == 1:
            num_triangles += 1
    return num_triangles

if __name__ == '__main__':
    
    
    lower_limit = 12
    upper_limit = 15000
    
    
    
    start = perf_counter()
    total_triangles = count_triangles(lower_limit, upper_limit)
    end = perf_counter()
    
    
    print("Total number of triangles:", total_triangles)
    print(f"Elapsed: {round((end - start), 2)} s")
