import sys, math
max = int(sys.argv[1])
index = 1
count = 0
found = False
maxDivCount = 0
while index<=max:
    count = count+index
    #print(count,end=": ")
    divcount = 0
    for x in range(1,int(math.sqrt(count)+1)): # for the future: remember devisors come in pairs! you only have to do brute-force style up to the square root of the number, then you can check if the number devided by the found devisors gives you new ones.
        if count % x == 0:
            divcount+=1
            d = count/x
            if d == int(d):
                divcount+=1
    if divcount>maxDivCount:
        maxDivCount = divcount
        print(str(count)+" there are "+str(divcount))
    index +=1
