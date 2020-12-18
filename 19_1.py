dic_non_leap = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
dic_leap = {'Jan':31, 'Feb':29, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
count = 0
days = 0
dull = 0
count_kill = 0
def year(a):
    if a % 4 == 0:
        if a % 100 == 0 and a % 400 != 0:
            return dic_non_leap
        else:
            return dic_leap
    else:
        return dic_non_leap

# 1/1/1900 was Monday
years = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i in range(1900, 2001):
    for l in years:
        days+=year(i)[l]
        if days % 7 == 6:
            count+=1
for m in years:
    dull+=year(1900)[m]
    if dull % 7 == 6:
        count_kill+=1

print(f'the total is {count-count_kill}')