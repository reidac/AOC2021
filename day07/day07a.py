filename = "input.txt"

if __name__=="__main__":
    f = open(filename,"r")
    l = f.readline()[:-1]
    plist = eval('['+l+']')

    vlist = [0]*max(plist)

    for p in plist:
        for i in range(len(vlist)):
            vlist[i]+=abs(p-i)

    min_res = min(vlist)
    print("Minimal fuel cost: ", min_res)
    
