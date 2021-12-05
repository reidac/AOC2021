
class Board:
    def __init__(self):
        self.data = {}
        self.selections = set()
        self.rows = 0
    def addrow(self,lst):
        for v in zip(range(len(lst)),lst):
            try:
                self.data[ v[1] ].append( (self.rows,v[0]) )
            except KeyError:
                self.data[ v[1] ] = [ (self.rows,v[0]) ]
        self.rows += 1
    def select(self,val):
        pass
    def win(self):
        pass
    def __repr__(self):
        # Representation is inefficient but also infrequent.
        res = ''
        for r in range(5):
            res += "-- "
            for c in range(5):
                for (k,v) in self.data.items():
                    if (r,c) in v:
                        res += " "+str(k)+" "
                        break
            res += '\n' 
        return res

filename = "input.txt"

if __name__=="__main__":
    boards = set()
    b = None
    f = open(filename,'r')
    drawline = f.readline()[:-1]
    draws = eval('['+drawline+']')
    print(draws)
    for l in f:
        tl = l[:-1]
        if len(tl)==0:
            b = Board()
            boards.add(b)
        else:
           vs = [ int(x) for x in l.split() ]
           b.addrow(vs)

    for b in boards:
        print(b)
