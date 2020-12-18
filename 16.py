"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""
import time
start = time.time()

# first, figure out 2^1000
# second, seperate each digit
# third, sum all digits
t = 0
a = str(2**1000)
for i in a:
    t+=int(i)
    #sum all digits
print(f'the answer is {t}')

end = time.time()
print(end-start)