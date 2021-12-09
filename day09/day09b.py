
filename = "input.txt"
adjacencies = [(-1,0),(1,0),(0,1),(0,-1)]

def lowerthan(v,nr,nc): # Are we lower than this neighbor?
    try:
        nv = map[nr,nc]
    except KeyError:
        return True
    return v<nv


# Recursive basin traversal.  In principle this can
# over-count the basin rims, if e.g. they top out at
# a value that is not 9, but apparently the input set
# does not do this.  Which means the "nv>v" test
# is redundant, one could simply build the grid
# without the 9's and count the size of the connected
# components, and multiply those.

def basin(rim,body): # Find all the points in the basin.
    if len(rim)==0:
        return len(body)
    else:
        frontier = set()
        for p in rim:
            v = map[p]
            for a in adjacencies:
                np = (p[0]+a[0],p[1]+a[1])
                try:
                    nv = map[np]
                except KeyError:
                    pass
                else:
                    if (nv>v) and (nv!=9) and not (np in body):
                        frontier.add(np)
                        body.add(np)
        return basin(frontier,body)
                    
    
    
if __name__=="__main__":
    f = open(filename,"r")
    map = {}
    row_index = 0
    for l in f:
        column_index = 0
        for v in [ int(x) for x in l[:-1]]:
            map[(row_index,column_index)] = v
            column_index += 1
        row_index += 1
            
    res = 0
    lowpts = set()
    for r in range(row_index):
        for c in range(column_index):
            v = map[r,c]
            lowpt = True
            for (dr,dc) in adjacencies:
                lowpt &= lowerthan(v,r+dr,c+dc)
            if lowpt:
                lowpts.add( (r,c) )
    basin_list = []
    for lp in lowpts:
        init_rim = set()
        init_rim.add(lp)
        init_bdy = set()
        init_bdy.add(lp)
        basin_list.append(basin(init_rim,init_bdy))

    basin_list.sort()
    res = basin_list[-1]*basin_list[-2]*basin_list[-3]
    print("Product of the three largest basins: ", res)
