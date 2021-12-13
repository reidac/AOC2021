
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
        pass

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
                break

    fold(dct,axis,level)
    print("Visible spots after one fold: ", len(dct))
