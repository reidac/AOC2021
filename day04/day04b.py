
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
        if val in self.data.keys():
            self.selections.add(val)
    def win(self):
        row_data = {}
        col_data = {}
        for s in self.selections:
            for rc in self.data[s]:
                (r,c) = rc
                try:
                    row_data[r]+=1
                except KeyError:
                    row_data[r]=1
                try:
                    col_data[c]+=1
                except KeyError:
                    col_data[c]=1
        if ( 5 in row_data.values()) or (5 in col_data.values() ):
            return True
        return False
    def score(self,lastval):
        # Sum of all the unselected numbers, times the last value.
        sum = 0
        for v in self.data.keys():
            if not (v in self.selections):
                sum += v
        return sum*lastval
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

    done = False
    for d in draws:
        for b in boards:
            b.select(d)
            if (b.win()):
                print("First winning board's score is ", b.score(d))
                done = True
                break
        if (done):
            break


