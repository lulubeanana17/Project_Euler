"""
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
# this is using buinomial coefficient
from time import time
from math import factorial

start = time()

def routes(a, b):
    return factorial(a+b)/(factorial(a)*factorial(b))

print(f'the total ways to reach to te bottom right corner is {routes(20,20)}')

end = time()

print(end-start)