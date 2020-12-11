# 2520 is the smallest number 
# that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?
while True:
    # while loop
    a = 1
    # the number will be divided
    t = 0
    # recognise whether it is the number or not

    for i in range(1,21):
        # 2otimes division
        if a % i != 0:
            # if a has remainder
            t += 1
            # t add 1
    
    if t == 0:
        # t=0 means that it is the number is divisible 
        print(f'{a} is the samllest number that is divisible by all of the numebrs from 1 to 20')
        break
    # end
    else:
        a += 1
        # add 1 to a
        continue
    # go back to first