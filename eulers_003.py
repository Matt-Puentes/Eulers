#prime factorization
def primeFac(n):
    primeFacs = []
    i = 2
    while i*i<=n:
        while n%i == 0:
            primeFacs.append(i)
            n//=i
        i+=1
    if n>1:
        primeFacs.append(n)
    return primeFacs
import sys

n = int(sys.argv[1])
print(str(primeFac(n)))
