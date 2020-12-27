A = []

for a in range(2,101):
    for b in range(2,101):
        answer = a**b
        A.append(answer)
A = sorted(set(A))
print(len(A))