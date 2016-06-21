import sys
n = int(sys.argv[1])

count = 1
for i in range(0,n):
    count = count * (i+1)
    print(str(i+1)+" "+str(count))

ccount = 0
for i in str(count):
    ccount+=int(i)

print(ccount)
