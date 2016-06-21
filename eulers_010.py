import sys,math
n = int(sys.argv[1])-1
count = 2
while n>2:
    x = 3
    broken = False
    while x <= math.sqrt(n) and not broken:
        if n%x == 0:
            broken = True
        x+=2
    if not broken:
        count += n
        print(str(n)+" "+str(count))
    n-=2
