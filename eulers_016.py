import math
count = 0
for i in str('%f' % math.pow(2,1000)): # the whole %f thing makes it a float
    if(i is not "."):
        count+=int(i)
print(count)
