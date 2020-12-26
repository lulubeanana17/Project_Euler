def prime(n):
    primes = []
    for m in range(2,n+1):
        t = 0
        for i in range(2,n+1):
            if m % i == 0:
                t+=1
        if t == 1:
            primes.append(m)
    return primes

prime_numbers = prime(1000)

# both are positive case
maximum1 = 0
maximum2 = 0
answer1 = 0
answer2 = 0

for a in prime_numbers:
    for b in prime_numbers:
        n = 0
        count = 0

        while True:
            if n**2 + a*n + b in prime_numbers:
                count += 1
            else:
                if count > maximum1:
                    maximum1 = count
                    answer1 = a*b
                break
            n+=1

for a in prime_numbers:
    for b in prime_numbers:
        n = 0
        count = 0

        while True:
            if n**2 - a*n + b in prime_numbers:
                count += 1
            else:
                if count > maximum2:
                    maximum2 = count
                    answer2 = -a*b
                break
            n+=1

if maximum1 > maximum2:
    print(answer1)
else:
    print(answer2)