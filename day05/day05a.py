
def interator(i1,i2):
    if (i2<i1):
        low = i2
        high = i1
    else:
        low = i1
        high = i2
    for v in range(low,high+1,1):
        yield v

filename="input.txt"

grid = {}

if __name__=="__main__":
    f = open ('input.txt')
    for l in f:
        flds = l[:-1].split()
        (x0,y0) = eval('('+flds[0]+')')
        (x1,y1) = eval('('+flds[2]+')')
        if (x0==x1):
            for y in interator(y0,y1):
                try:
                    grid[(x0,y)] += 1
                except KeyError:
                    grid[(x0,y)] = 1
        elif (y0==y1):
            for x in interator(x0,x1):
                try:
                    grid[(x,y0)] += 1
                except KeyError:
                    grid[(x,y0)] = 1


    vset = [ x for x in grid.values() if x > 1 ]
    print("Crossing points: ", len(vset))
