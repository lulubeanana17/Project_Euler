# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

a = []
t = 0
b = int(input('enter the number you want to sum all below the number : '))
# make an empty list, assign t is 0 to count, input the user answer
if b < 2:
    print('enter the number over 1 please')
    # for loop below, b should be bigger than 1
else:
    for i in range(2, b+1):
        for l in range(2,i+1):
            if i % l == 0:
                t += 1
        if t == 1:
            # t = 1 means it is a prime number
            a.append(i)
        t = 0

print(f'the sum of the primes below {b} is {sum(a)}')