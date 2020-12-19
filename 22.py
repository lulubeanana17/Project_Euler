"""
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 

So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import time
start = time.time()

count = 0
total = []

with open('C:/Users/admin1/Desktop/22.txt') as f:
    data = f.read()

data = data.strip().split(',')
data.sort()

for i in data:
    count+=1
    num = 0
    for l in i[1:-1]:
        num+=(ord(l)-64)
    total.append(num*count)

end = time.time()
print(f'the total of all the name scores in the file is {sum(total)}')
print(end-start)