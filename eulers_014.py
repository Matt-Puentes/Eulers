maxTerms = 0
for num in range(13,1000000):
    o = num
    count = 1
    while int(num) is not 1:
        if num % 2==0:
            num = num/2
        else:
            num = num*3+1
        count +=1
    if(count>maxTerms):
        print(str(o)+" has "+str(count)+" terms")
        maxTerms=count
