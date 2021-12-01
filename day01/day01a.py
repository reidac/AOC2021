
if __name__=="__main__":
    f = open("input.txt","r")
    ct = 0
    vo = 0
    dc = 0 # Descent counter.
    for l in f:
        nv = int(l)
        
        if (ct<2):
            if (v>vo):
                dc += 1
        ct += 1
        vo = v

    print("Depth increment count: ", dc)
