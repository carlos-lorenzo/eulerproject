"""
Problem 4:
Find the largest palindrome made from the product of two 3 digit numbers.
"""

def is_palindrome(n: int) -> bool:
    """
    Checks weather a number is palindrome or not

    Args:
        n (int): Number to check

    Returns:
        bool: Is palindrome? True/False
    """
    
    return str(n) == str(n)[::-1]


def find_largest_palindrome_product(l: int) -> int:
    """
    Finds the largest product of two l-digit numbers which results in a palindrome
    
    O(n^2)

    Args:
        l (int): Length of number i.e. number of digits

    Returns:
        int: Larget palindrome number found
    
    """  
    
    largest_palindrome: int = 0
    
    for i in range(10**(l-1) ,10**l):
        for j in range(10**(l-1), 10**l):
            current_nun = i * j
            if is_palindrome(current_nun):
                if current_nun > largest_palindrome:
                    largest_palindrome = current_nun
    
    
    return largest_palindrome
        
        
print(find_largest_palindrome_product(l=3))