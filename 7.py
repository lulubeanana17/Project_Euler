n = 0 
# check the number is prime or not from 2 to infinite
t = 0
# distinguish it is prime or not
c = 0
# how many prime number we have until now
while True:
    n += 1
    # check all number from 1
    if n > 1:
        # check the number from 2
        for i in range(1,n+1):
            if n % i == 0:
                t += 1
                # if divided with 0, add 1 to t
        if t == 2:
            # t == 1 means it is prime number
            c += 1
            # count c +1
        t = 0
        # initialization t
    if c == 7:
        # 10001st prime number
        print(n)
        break
    # end the program
