import math
i = 13
c = 1
found = False
for i in range(3,10000000,2):
    #print(str(i)+" "+str(int(math.sqrt(i))))
    x = 3
    broke = False
    for x in range(3,int(math.sqrt(i))+1,2):
        if i % x == 0:
            #print("failed on "+str(x))
            broke = True
    if not broke:
        c+=1
        if c<10:
            print("fOUND IT "+str(i)+" "+str(c))
        if c==10001:
            print("fOUND IT "+str(i)+" "+str(c))
            exit()
