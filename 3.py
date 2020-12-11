# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# A Prime Number is:
# a whole number greater than 1 that can not be made by multiplying other whole numbers
# "Factors" are the numbers you multiply together to get another number
# "Prime Factorization" is finding 
# which prime numbers multiply together to make the original number.
prime_number = []
prime_factor = []
t = 0
a = 600851475143

for i in range(2, 10001):
    for b in range(1, 10001):
        if i % b == 0:
            t+=1
    if t == 2:
        prime_number.append(i)
    t = 0

# distinguish each prime number can divide the given number or not
# if a prime number can divide the give number, divide them
# after that, try again
# at the last, if the last number is prime number, show the list
# show the biggest number by using max function

for i in prime_number:
    if a % i == 0:
        prime_factor.append(i)
print(prime_factor)
print(f'the largest prime factor of the number 600851475143 is {max(prime_factor)}')