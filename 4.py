# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999
e = []
while True:
    # to multiple 999 to 1
    for i in range(1,a):
        # to input 1 to 999
        if b > 0:
            c = str(i*b) 
        # to use index
            d = len(str(i*b))
        # using index
            if d % 2 == 0:
            # when it is even
                if c[:int(d/2) - 1] == c[-1:-int(d/2)]:
                # whether first-middle and middle-end is the same or not
                    e.append(i*b)
                # if it is palindrome, append to e
            if d % 2 != 0:
            # when it is odd
                if c[:(d//2)] == c[-1:-(d//2 + 1)]:
                # whether first-middle and middle-end is the same or not
                    e.append(i*b)
                # if it is palidrome, append to e
        else:
            break
    b -= 1
try:
    print(f'the largest palindrome made from the product of two 3-digit numbers is {max(e)}')
except ValueError:
    print('you don"t have any palindromic numbers')