
# filename = "test.txt"
filename = "input.txt"

class Node:
    def __init__(self,coords):
        self.coords = coords
        self.cost = None # Infinite, essentially.
        self.goal = False
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
                if nb_node in nodelist:
                    new_cost = current.cost + grid[nb_coord]
                    if (nb_node.cost is None) or (new_cost < nb_node.cost):
                        nb_node.cost = new_cost
        # Updating of neighbor costs is complete. Logistics from here.
        if (current.goal):
            done = True # Redundant, we're about to leave...
            return current.cost
        else:
            nodelist = nodelist[1:] # Lead node has now been visited.
            nodelist.sort()
        
            


if __name__=="__main__":
    f = open(filename, "r")
    grid = {}
    node_dct = {}
    node_lst = []
    row_index = 0
    for l in f:
        col_index = 0
        for c in l[:-1]:
            grid[(row_index,col_index)] = int(c)
            node = Node( (row_index,col_index) )
            node_lst.append(node)
            node_dct[ (row_index,col_index) ] = node
            col_index += 1
        row_index += 1

    node_lst[0].cost = 0
    node_dct[ (row_index-1,col_index-1) ].goal = True 
    res = traverse(grid,node_lst,node_dct)
    print(res)
