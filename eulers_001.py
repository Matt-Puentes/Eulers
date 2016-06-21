count = 0
for i in range(0,1000):
    print(i)
    if(i % 3 == 0 or i % 5 == 0):
        print(i)
        count+=i
print(count)
