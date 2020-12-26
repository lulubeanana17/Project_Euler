the_greatest_num = 0

for i in range(983,984):
    A = []
    start_num = 10 # basically, it sets as 0.----
        
    while True:
        if start_num % i == 0:
            A.append(start_num//i)
            if the_greatest_num < len(A):
                the_greatest_num = len(A)
            break 

        elif start_num % i == 1:
            A.append(start_num//i)
            if the_greatest_num < len(A):
                the_greatest_num = len(A)
            break

        else:
            if start_num < i:
                start_num = start_num*10
                A.append(0)
                
            else:
                A.append(start_num//i)
                start_num = (start_num % i)*10

print(f'the largest digits number is {the_greatest_num}')