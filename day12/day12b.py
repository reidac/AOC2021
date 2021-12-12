
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
            
if __name__=="__main__":
    f = open(filename,"r")
    net = Net()
    for l in f:
        linkends = l[:-1].split('-')
        net.add_link(linkends[0],linkends[1])


    base_path = Path()
    base_path = base_path.append('start')
    pathlist = [ base_path ]
    done = False
    while not done:
        done = True
        newpl = []
        for p in pathlist:
            if p[-1]=='end':
                newpl.append(p) # Unmodified, path is complete.
            else:
                scsrs = net.nbrs(p[-1])
                for s in scsrs:
                    append_res = p.append(s)
                    if append_res is not None:
                        newpl.append(append_res)
                        done = False
        pathlist = newpl
    print("Number of paths: ", len(pathlist))

