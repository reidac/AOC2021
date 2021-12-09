
filename = "input.txt"
adjacencies = [(-1,0),(1,0),(0,1),(0,-1)]

# Recursive basin traversal. Just find the
# connected component, the map has been built
# without the "9" elements.  This is about 30%
# faster than actually comapring values to
# say in the basin.
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
                    if not nv:
                        frontier.add(np)
                        body.add(np)
                        map[np]=True
        return basin(frontier,body)
                    
    
    
if __name__=="__main__":
    f = open(filename,"r")
    map = {}
    row_index = 0
    for l in f:
        column_index = 0
        for v in [ int(x) for x in l[:-1]]:
            if (v!=9):
                map[(row_index,column_index)] = False
            column_index += 1
        row_index += 1
            
    basin_list = []
    for lp in map.keys():
        if not map[lp]: # Point is not in a basin yet.
            init_rim = set()
            init_rim.add(lp)
            init_bdy = set()
            init_bdy.add(lp)
            basin_list.append(basin(init_rim,init_bdy))

    basin_list.sort()
    res = basin_list[-1]*basin_list[-2]*basin_list[-3]
    print("Product of the three largest basins: ", res)
