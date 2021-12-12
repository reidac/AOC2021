
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
            

if __name__=="__main__":
    f = open(filename,"r")
    net = Net()
    for l in f:
        linkends = l[:-1].split('-')
        net.add_link(linkends[0],linkends[1])


    pathlist = [ ['start'], ]
    done = False
    while not done:
        done = True
        newpl = []
        for p in pathlist:
            if p[-1]=='end':
                newpl.append(p) # Unmodified, we are done.
            else:
                scsrs = net.nbrs(p[-1])
                for s in scsrs:
                    if s.islower() and s in p:
                        pass
                    else:
                        newpl.append(p+[s])
                        done = False
        pathlist = newpl
    print("Number of paths: ", len(pathlist))

