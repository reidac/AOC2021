
filename = "input.txt"
adjacencies = [(-1,0),(1,0),(0,1),(0,-1)]

def lowerthan(v,nr,nc): # Are we lower than this neighbor?
    # list[-1] is valid Python but invalid on the map!
    # (Shouda used a dict?)
    if (nr<0) or (nc<0):
        return True
    try:
        nv = map[nr][nc]
    except IndexError:
        return True
    return v<nv
    

if __name__=="__main__":
    f = open(filename,"r")
    map = []
    for l in f:
        row = [ int(x) for x in l[:-1]]
        map.append(row)

    res = 0
    for r in range(len(map)):
        for c in range(len(map[0])):
            v = map[r][c]
            lowpt = True
            for (dr,dc) in adjacencies:
                lowpt &= lowerthan(v,r+dr,c+dc)
            if lowpt:
                res += (v+1)
    print("Sum of risk levels: ", res)
