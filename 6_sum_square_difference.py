"""
Problem 6:
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


square_sums = sum([num**2 for num in range(1, 101)])
sum_square = sum([num for num in range(1, 101)])**2

print(sum_square - square_sums)