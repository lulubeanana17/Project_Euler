b = 0
# the sum of from 1 to 100
a = [a**2 for a in range(1,101)]
# list of a**2 from 1 to 100
for i in range(1, 101):
    b += i
    # add from 1 to 100 to b

print(f'the answer is {b**2 - sum(a)}')