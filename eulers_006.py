squarecount = 0
i=1
while i<=100:
    squarecount+=i*i
    i+=1
addcount = 0
i=1
while i<=100:
    addcount+=i
    i+=1
addcount = addcount*addcount

print(str(squarecount)+" "+str(addcount))
print(str(squarecount-addcount))
