"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
def factorial(a):
    number = 1
    for i in range(1,a):
        number*=i
    return number
numbers = 0

the_sum = str(factorial(100))
for l in the_sum:
    numbers+=int(l)
print(f'the sum of the digits in the number 100! is {numbers}')