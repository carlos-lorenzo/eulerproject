def sqrt_high_precision(n: int, decimal_places: int) -> int:
    """
    Computes square root of a number to high precision using Newton Rapson's method.
    Not that the result is scaled by 10^decimal_places to overcome floating point math limitation

    Args:
        n (int): Number to which find square root of
        decimal_places (int): Number of decimal places in answer

    Returns:
        int: Square root multiplied by 10^decimal_places
    """
    
    
    n_scaled = n * 10**(2*decimal_places)
    x = n_scaled
    
    while True:
        y = (x + n_scaled // x) // 2
        if y >= x:
            return x
        x = y


def sum_digits(n: float) -> int:
    """
    Finds sum of digits in number

    Args:
        n (float): Number for which to find sum of digits

    Returns:
        int: Sum of digits in number
    """
    return sum([int(digit) for digit in str(n)])
    

SQUARES = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sum_square_nums = 0


for n in range(1, 100):
    if n not in SQUARES:
        sum_square_nums += sum_digits(sqrt_high_precision(n, 99))
        
        
print(sum_square_nums)