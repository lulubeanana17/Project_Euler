"""
A perfect number is a number 
for which the sum of its proper divisors is exactly equal to the number. 

For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors 
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 

By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 

However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers 
which cannot be written as the sum of two abundant numbers.
"""
abundant_numbers = []
# all list of abundant numbers under 28124
the_sum_of_two = []
# all list of two abundatn numebers under 28124
the_sum_of_all = []
# all list of all numbers

def sum_divisors(a):
    divisor = []
    for i in range(1,a):
        if a % i == 0:
            divisor.append(i)
    return sum(divisor)
# the sum of divisors of given number

def abundant_number(b):
    if sum_divisors(b)>b:
        abundant_numbers.append(b)
# figure out the abundant number of given number

for l in range(1, 28124):
    abundant_number(l)

for m in abundant_numbers:
    for n in abundant_numbers:
        if m+n<28124:
            the_sum_of_two.append(m+n)
# the sum of two abundant numbers under 28124

for o in range(1,28124):
    the_sum_of_all.append(o)

print(f'the answer is {sum(the_sum_of_all)-sum(set(the_sum_of_two))}')