
if __name__=="__main__":
    f = open("input.txt","r")
    ct = 0
    dc = 0
    vset = [0,0,0]
    dc = 0 # Descent counter.
    for l in f:
        nv = int(l)
        if (ct<3):
            vset[ct]=nv
            ct += 1
        else:
            osum = sum(vset)
            vset[ct%3]=nv
            nsum = sum(vset)
            
            if (nsum > osum):
                dc += 1
            ct += 1

    print("Depth increment count: ", dc)
