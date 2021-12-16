
# filename = "test.txt"
filename = "input.txt"

class Node:
    def __init__(self,coords):
        self.coords = coords
        self.cost = None # Infinite, essentially.
        self.goal = False
        self.visited = False
    def __lt__(self,other): # For sorting.
        if (other.cost is None):
            return True
        if (self.cost is None):
            return False
        return (self.cost < other.cost)
    def __repr__(self):
        return "Node("+str(self.coords)+":"+str(self.cost)+")"
    
def traverse(grid,nodelist,nodeindex):
    done = False
    while not done:
        current = nodelist[0]
        for delta in [(1,0),(-1,0),(0,1),(0,-1)]:
            nb_coord = (current.coords[0]+delta[0],
                        current.coords[1]+delta[1])
            try:
                nb_node = nodeindex[nb_coord]
            except KeyError:
                pass
            else:
                if not(nb_node.visited):
                    new_cost = current.cost + grid[nb_coord]
                    if (nb_node.cost is None) or (new_cost < nb_node.cost):
                        nb_node.cost = new_cost
                    if not (nb_node in nodelist):
                        nodelist.append(nb_node)
        # Updating of neighbor costs is complete. Logistics from here.
        if (current.goal):
            done = True # Redundant, we're about to leave...
            return current.cost
        else:
            current.visited = True
            nodelist = nodelist[1:]
            nodelist.sort()

if __name__=="__main__":
    f = open(filename, "r")
    keyset = set()
    grid = {}
    node_dct = {}
    node_lst = []
    row_index = 0
    for l in f:
        col_index = 0
        for c in l[:-1]:
            grid[(row_index,col_index)] = int(c)
            node = Node( (row_index,col_index) )
            node_dct[ (row_index,col_index) ] = node
            keyset.add( (row_index,col_index) )
            col_index += 1
        row_index += 1

    for rx in range(5):
        for cx in range(5):
            if ((rx!=0) or (cx!=0)):
                for k in keyset:
                    v = grid[k]
                    nv = (((v-1)+rx+cx)%9)+1
                    nc = (k[0]+rx*row_index,k[1]+cx*col_index)
                    grid[nc] = nv
                    node = Node(nc)
                    node_lst.append(node)
                    node_dct[nc] = node

    node_dct[ (row_index*5-1,col_index*5-1) ].goal = True
    node_lst = [ node_dct[(0,0)] ]
    node_lst[0].cost = 0
    
    res = traverse(grid,node_lst,node_dct)
    print(res)
