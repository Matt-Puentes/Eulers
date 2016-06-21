import sys
n = int(sys.argv[1])
while n > 0:
    works = []
    failed = False
    x = 20
    while x>0:
        #print("   "+str(x))
        if n%x!=0:
            failed=True
            break
        works.append(x)
        x-=1
    if failed == False:
        print("solution: "+ str(x))
        print(str(n) + "  "+ str(works))
        exit()
    if len(works) > 8:
        print(str(n) + "  "+ str(works))
    n+=20
