answer = 0
for i in range(2, 6*9**5+1):
    # fifth power of digits 
    # 99999 = 5x9^5 = 295245
    # 999999 = 6x9^5 = 354294
    # the maximum is 6digits of the numbers
    if sum([int(x)**5 for x in str(i)])==i:
        answer+=i

print(answer)