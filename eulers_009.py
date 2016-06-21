import math
n = 3
found = False
while not found:
    for i in range(330):
        d = math.sqrt(n*n + i*i)
        if (d == int(d)):
            if(n+i+d==1000):
                print(str(n)+" "+str(n+1)+" "+str(n+2)+" ")
                print("answer")
                print(n*i*d)
    n+=1
