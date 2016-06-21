import sys
def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)

n = int(sys.argv[1])-1+2
print(fib(n))

i = 2
count = 0
latest = 0
while latest < 4000000:
    latest = fib(i)
    print(latest,end=" ")
    if latest < 4000000 and latest % 2 == 0:
        count = count + latest
    i+=1
print("count "+str(count))
