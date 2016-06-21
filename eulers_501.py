import sys,math
OverallCount = 0
#print(sys.argv[1])
#for i in range(10000000 , int(sys.argv[1])):
#i = 10e6
i = 0
while i<=100 :
    print(i)
    count = 0
    x=2
    while x<(math.sqrt(i)):
        if i % x is 0:
            print("normal")
            count=count+1
            if i != (x / i):
                print("extra!")
                count=count+1
        x+=1

    print("count"+str(count))
    count = count+2
    #print("count is"+str(count))
    if count == 8:
        OverallCount+=1
        print(str(i)+" works")
    i+=1

print("there are "+str(OverallCount))
