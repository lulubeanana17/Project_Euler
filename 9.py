# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#while loop
#a=1 b=a+1 c=1000-(a+b)
#if a^2+b^2=c^2 print(abc)
#b+=1 c-=1
#if b>=c a+=1 b=a+1
#if a>=b break
a = 1
b = a+1
c = 12 - (a+b)
while True:
    #while loop
    if a**2 + b**2 == c**2:
        # find the theory
        print(a*b*c)
        break
    elif b >= c:
        #if b = c, a+=1
        a += 1
    elif a >= b:
        # if a = b, the end
        break
    else:
        b+=1
        # b+=1 again