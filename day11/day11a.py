
filename = "input.txt"
# filename = "special.txt"
# filename = "test.txt"

adjacencies = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def increment(grid):
    for k in grid.keys():
        grid[k]+=1
    res = 0
    done = False
    flashed = set()
    while not done:
        delta = 0
        for k in grid.keys():
            if (not (k in flashed)) and (grid[k]>9):
                delta += 1
                flashed.add(k)
                for a in adjacencies:
                    try:
                        grid[(k[0]+a[0],k[1]+a[1])] += 1
                    except KeyError:
                        pass
        if (delta==0):
            done = True
        else:
            res += delta

    for k in flashed:
        grid[k]=0
            
    return res

def draw(grid,rows,cols):
    for c in range(cols):
        ln = ""
        for r in range(rows):
            ln += '{0:3d}'.format(grid[r,c])
        print(ln)
                       
    
if __name__=="__main__":
    grid = {}
    f = open(filename,"r")
    col_index = 0
    for l in f:
        row_index = 0
        for ch in l[:-1]:
            grid[row_index,col_index] = int(ch)
            row_index += 1
        col_index += 1

    sum = 0
    for i in range(100):
        sum += increment(grid)
        
        
    print("Total flashes in all the steps: ", sum)
    
