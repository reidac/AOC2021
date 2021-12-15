filename = "input.txt"
steps = 10
# filename = "test.txt"
# steps = 10
def insertion(tpl,rules):
    iset = {}
    for i in range(len(tpl)-1): # No insertion after last 
        for rule in rules[tpl[i]]:
            if tpl[i+1]==rule[0]:
                iset[i+1] = rule[1]
    klist = [x for x in iset.keys()]
    klist.sort()

    count = 0
    for k in klist:
        tpl.insert(k+count,iset[k])
        count += 1

if __name__=="__main__":
    f = open(filename,"r")
    template = [c for c in f.readline()[:-1]]

    blank = f.readline()

    rules = {}
    for l in f:
        try:
            rules[l[0]].append( l[1]+l[-2] )
        except KeyError:
            rules[l[0]] = [ l[1]+l[-2] ]

    hist = {}
    for c in template: # Capture the segment endpoints.
        try:
            hist[c] += 1
        except KeyError:
            hist[c] = 1
    for i in range(len(template)-1):
        subt = template[i:i+2]
        for i in range(steps):
            insertion(subt,rules)
        for c in subt[1:-1]: # Omit endpoints, captured earlier.
            try:
                hist[c]+=1
            except KeyError:
                hist[c]=1

    maxv = None
    minv = None
    for v in hist.values():
        if (maxv is None) or (v>maxv):
            maxv = v
        if (minv is None) or (v<minv):
            minv = v
    print("Max - min: ", maxv-minv)
