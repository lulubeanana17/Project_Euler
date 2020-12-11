# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
fibo = [1,2]
for i in range(400):
    a = fibo[i] + fibo[i+1]
    fibo.append(a)
b = [i for i in fibo if i % 2]
print(sum(b))
# until four million, it brings memory error. Python is not suitable for numerical calculation.