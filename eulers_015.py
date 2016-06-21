''' this random path genrator is cool! but i dont think its the best way to '''
'''solve this problem. In fact i dont think it works at all! This is more of'''
'''a math problem anyway. Heres a brief explanation of how you managed to   '''
'''solve it: the path is always 40 units long, and each unit has to either  '''
'''be down or right. So the problem is just how many combinations of down   '''
'''and right can you have with 20 downs and 20 rights. Thats a combination  '''
'''formula which is 40! / (20! (40 - 20)!). Credit goes to'''
'''http://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/'''
import random
types = []
found = False
while not found:
    path = []
    pos = (0,0)
    while pos[0]<20 or pos[1]<20:
        x = 0
        y = 0
        if(pos[0]==20):
            y=1
        elif(pos[1]==20):
            x=1
        else:
            d = random.random()
            if(d>0.50):
                x=1
            else:
                y=1
        pos = (pos[0]+x,pos[1]+y)
        #print(str(x)+","+str(y)+" "+str(pos))
        path.append(pos)
    if path not in types:
        types.append(path)
        print(path)
        print(len(types))
