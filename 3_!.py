number = 13195

for prime_factor in range(2, int(number**(0.5))+1):
    while number % prime_factor == 0:
        number /= prime_factor
        if number == 1 or number == prime_factor:
            print(prime_factor)
            break