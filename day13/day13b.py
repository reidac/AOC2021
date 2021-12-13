
#
#    x ->
# y
# |
# v
#

filename = "input.txt"

def fold(dct,axis,level):
    folds = {}
    dlist = []
    if axis=='x':
        # Fold leftwards, higher x's get lowered.
        for k in dct.keys():
            if k[0]>level:
                dlist.append(k)
                folds[(2*level-k[0],k[1])] = 1

    elif axis=='y':
        # Fold upwards, higher y's get lowered.
        for k in dct.keys():
            if k[1]>level:
                dlist.append(k)
                folds[(k[0],2*level-k[1])] = 1

    for k in folds.keys():
        try:
            dct[k]+=1
        except KeyError:
            dct[k]=1
    for k in dlist:
        dct.pop(k)
        
    
                    
if __name__=="__main__":
    dct = {}
    f = open(filename,"r")
    for l in f:
        rl = l[:-1]
        flds = rl.split(',')
        if len(flds)==2:
            r = int(flds[0])
            c = int(flds[1])
            dct[(r,c)] = 1
        else:
            if len(rl)!=0:
                flds = rl.split('=')
                axis = flds[0][-1]
                level = int(flds[1])
                fold(dct,axis,level)

    xmin = None
    xmax = None
    ymin = None
    ymax = None
    for k in dct.keys():
        if (xmin is None) or (k[0]<xmin):
            xmin = k[0]
        if (xmax is None) or (k[0]>xmax):
            xmax = k[0]
        if (ymin is None) or (k[1]<ymin):
            ymin = k[1]
        if (ymax is None) or (k[1]>ymax):
            ymax = k[1]

    for r in range(ymin,ymax+1):
        str = ""
        for c in range(xmin,xmax+1):
            if (c,r) in dct.keys():
                str += '#'
            else:
                str += '.'
        print(str)
        
