count = 0
for a in range(3):
    # 100
    for b in range(int((200-100*a)/50) + 1):
        #50
        for c in range(int((200-100*a-50*b)/20)+1):
            #20
            for d in range(int((200-100*a-50*b-20*c)/10)+1):
                #10
                for e in range(int((200-100*a-50*b-20*c-10*d)/5)+1):
                    #5
                    for f in range(int((200-100*a-50*b-20*c-10*d-5*e)/2)+1):
                        #2
                        #1 is defined automatically
                        count+=1
print(count+1)
#+1 is when 200 is 1