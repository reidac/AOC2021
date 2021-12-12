
# filename = "tiny.txt"
# filename="test.txt"
filename = "input.txt"

class Net:
    def __init__(self):
        self.dct = {}
    def add_link(self,a,b):
        try:
            self.dct[a].append(b)
        except KeyError:
            self.dct[a]=[b]
        try:
            self.dct[b].append(a)
        except KeyError:
            self.dct[b]=[a]
    def nbrs(self,key):
        return self.dct[key]
            

class Path:
    # Stateful path that knows the appending rules. At most
    # one lower-case cave that isn't start or end can be
    # visited twice.
    def __init__(self):
        self.data = []
        self.twosmalls = False
    def append(self,node): # Returns a new Path instance or "None".
        if node.isupper():
            newp = Path()
            newp.data = self.data + [node]
            newp.twosmalls = self.twosmalls
            return newp
        if node.islower():
            if (node=='start') and (node in self.data):
                return None
            if (node in self.data):
                if self.twosmalls:
                    return None
                else:
                    newp = Path()
                    newp.data = self.data + [node]
                    newp.twosmalls = True
                    return newp
            else:
                newp = Path()
                newp.data = self.data + [node]
                newp.twosmalls = self.twosmalls
                return newp
    def __getitem__(self,key):
        return self.data[key]
    def __repr__(self):
        return "Path("+str(self.data)+")"

# Generator to generate all the valid paths arising from
# the input path.
def traverse(net,path):
    if path[-1]=='end':
        yield path
    else:
        for s in net.nbrs(path[-1]):
            ap = path.append(s)
            if ap is not None:
                for t in traverse(net,ap):
                    yield t
                    
                
            
    
if __name__=="__main__":
    f = open(filename,"r")
    net = Net()
    for l in f:
        linkends = l[:-1].split('-')
        net.add_link(linkends[0],linkends[1])


    base_path = Path()
    base_path = base_path.append('start')
    count = 0
    for p in traverse(net,base_path):
        count += 1
    print("Total number of paths: ", count)

