reader = open("eulers_067_triangle.txt","r")
read = []
for line in reader:
    read.append(line)

rows = []
for q in read:
    rows.append([int(i) for i in q.split(" ")])

#sssoooo this counts as checking every path, which is too slow.
#find new algorithm
maxDepth = len(rows)-1
def recursiveSearch(row, index, val):
    nodeCost = int(rows[row][index])
    if row == maxDepth:
        return val+nodeCost
    else:
        p1 = recursiveSearch(row+1,index,val+nodeCost)
        p2 = recursiveSearch(row+1,index+1,val+nodeCost)
        if(row<50):
            print(row)
        if p1>p2:
            return p1
        else:
            return p2

print(recursiveSearch(0,0,0))
