diagonal = 1001
total = 1
def a(n):
    if n >= 2:
        return a(n-1) + 8*(n-1)
    if n == 1:
        return 1

def b(n):
    if n >= 2:
        return b(n-1) + 2 + 8*(n-2)
    if n == 1:
        return 1

def c(n):
    if n >= 2:
        return c(n-1) + 4 + 8*(n-2)
    if n == 1:
        return 1

def d(n):
    if n >= 2:
        return d(n-1) + 6 + 8*(n-2)
    if n == 1:
        return 1

for i in range(2, int((diagonal+1)/2)+1):
    total+= a(i) + b(i) + c(i) + d(i)

print(total)