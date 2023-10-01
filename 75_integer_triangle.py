from tqdm import tqdm

def triplets_of_sum(n: int) -> int:
    sides = set()
    num_triplets = 0
    
    for a in range(1, n):
        # Calculate value of b
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)
 
        # The value of c = n - a - b
        c = n - a - b
        
        if a*a + b*b == c*c and b > 0 and c > 0:
            if a not in sides:
                print(a, b, c)
                num_triplets += 1
                sides.add(a)
                sides.add(b)
                sides.add(c)
            
    return num_triplets    



num_triangles = 0
 
triplets_of_sum(120)
 
"""for l in tqdm(range(12, 1_500_000)):
    if triplets_of_sum(l) == 1:
        num_triangles += 1"""
    