"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time
start = time.time()

times = {}
n = 0
for i in range(2, 1000000):
    # put all numbers from 2 to 1M
    t = 1
    # how many times they process
    origin_i = i
    # to put it in the dictionary
    while True:
        if i % 2 == 0:
            i = int(i/2)
        elif i % 2 != 0:
            i = int(3*i + 1)
            # regarding the formula
        t+=1
        if i == 1:
            # the end
            if t > n:
                times.clear()
                times[origin_i] = t
                n = t
                # if it is bigger than previous one, add new one
            break


print(f'the number that produces the longest chain is {times.keys()} and its sequences contain {times.values()}terms.')

end = time.time()

print(end - start)