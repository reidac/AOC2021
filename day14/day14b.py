filename = "input.txt"
# filename = "test.txt"
steps = 40

class Alphavec:
    def __init__(self):
        self.data = [0]*26
    def __getitem__(self,ltr):
        idx = ord(ltr)-ord('A')
        return self.data[idx]
    def __setitem__(self,ltr,v):
        idx = ord(ltr)-ord('A')
        self.data[idx]=v
    def __add__(self,other):
        res = Alphavec()
        res.data = [ x+y for (x,y) in zip(self.data,other.data) ]
        return res
    def __repr__(self):
        return str(self.data)

pdict = {}
def rpair(pair,icount): # Resolve one pair, with endpoints.
    try:
        return pdict[ (pair,icount) ]
    except KeyError:
        if icount==0:
            res = Alphavec()
            res[pair[0]]+=1
            res[pair[1]]+=1
            pdict[ (pair,icount) ] = res
            return res
        try:
            subst = rules[pair]
        except KeyError: # No substitution, we have bottomed out.
            res = Alphavec()
            res[pair[0]]+=1
            res[pair[1]]+=1
            pdict[ (pair,icount) ] = res
            return res
        else:
            r1 = rpair(pair[0]+subst,icount-1)
            r2 = rpair(subst+pair[1],icount-1)
            res = r1+r2
            res[subst]-=1 # Center was double-counted.
            pdict[ (pair,icount) ] = res
            return res
                    
if __name__=="__main__":
    f = open(filename,"r")
    template = f.readline()[:-1]

    blank = f.readline()
    rules = {}
    for l in f:
        rules[ l[0]+l[1] ] = l[-2]

    hist = Alphavec()
    for i in range(len(template)-1):
        hist += rpair(template[i:i+2],steps)

    for i in range(1,len(template)-1):
        hist[template[i]]-=1

    nzero = [ x for x in hist.data if (x!=0) ]
    print("Max minus min: ", max(nzero)-min(nzero))
    
