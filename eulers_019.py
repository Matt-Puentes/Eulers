week = ["Monday","Tuesday","Wendsday","Thursday","Friday","Satarday","Sunday"]
week = 1
count = 0
for i in range(1900,2000+1):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if i%4 == 0 and not i==1900:
        days[1]=29
    for z in days:
        for q in range(0,z):
            print(week)
            if not i==1900:
                if week == 7 and q == 0:
                    count+=1
                    print("yo"+str(count))
            if week < 7:
                week +=1
            else:
                week = 1
print("yo"+str(count))
