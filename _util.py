import math
class Util():
    def isPrime(Self, n):
        '''For given number, will return True if prime and False otherwise'''
        if n == 0 or n == 1 :
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(math.sqrt(n))+1):
            if n % x == 0:
                return False
        return True

    def listDevisors(Self, n):
        '''Will return a sorted list of all devisors for a given number n'''
        bigDivList = []
        divList = []
        for x in range(1,int(math.sqrt(n)+1)):
            if n % x == 0:
                divList.append(x)
                d = n/x
                if d == int(d):
                    bigDivList.append(int(d))
        if len(bigDivList) >= 1:
            for i in bigDivList[::-1]:
                divList.append(i)
        return divList
