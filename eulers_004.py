i = 998001
found = False
while found == False:
    i = i-1
    istr = str(i)
    if len(istr)<=6:
        #print(istr[:3] +" "+ istr[-3:][::-1])
        if istr[:3] == istr[-3:][::-1]:
            print(istr)
            q = 999
            while q>100:
                #print(q)
                ans = i/q
                if(int(ans) == ans):
                    if len(str(int(ans))) == 3:
                        print("answer found")
                        print(istr+" "+str(q)+" "+str(ans))
                        found = True
                q-=1
