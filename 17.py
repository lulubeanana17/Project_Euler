"""
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?
"""
# need at least three dictionary (1~9), (10~19), (20~90)
# change btw int and str
# for loop
import time
start = time.time()

dic_1_9 = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
dic_10_19 = {'10':3, '11':6, '12':6, '13':8, '14':8, '15':7, '16':7, '17':9, '18':8, '19':8}
dic_20_90 = {'2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
# number of letters of each number
# e.g. one = 3, ten = 3, twenty = 6
count = 0
# all sum of letters 1 to 1000
for i in range(1, 1001):
    if i < 10:
        count+=dic_1_9[str(i)]

    if i >= 10 and i < 20:
        count+=dic_10_19[str(i)]

    if i >= 20 and i < 1001:
        if len(str(i))==2:
            count+=dic_20_90[str(i)[0]]
            count+=dic_1_9[str(i)[1]]
            #20~99
        if len(str(i))==3:
            count+=(dic_1_9[str(i)[0]] + 7)
            # 7 is hundred
            if str(i)[1]!='0':
                if str(i)[1]=='1':
                    count+=(dic_10_19[str(i)[1:]]+3)
                    # 3 is and
                if str(i)[1]!='1':
                    count+=(dic_20_90[str(i)[1]]+3)
                    count+=dic_1_9[str(i)[2]]
                    # 3 is and
            if str(i)[1]=='0':
                if str(i)[2]=='0':
                    pass
                else:
                    count+=(dic_1_9[str(i)[2]]+3)
            # 100~999
        if i == 1000:
            count+=11

end=time.time()
print(f'the total letters used is {count}')
print(end-start)