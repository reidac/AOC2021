filename = "input.txt"

# Not thrilled with the n^2 algorithm.
# Histogram trick and memoization of the cost
# function take the timing from 0.740 s
# to 0.448 s, about a 60% speedup.

cost_dir = {}
def cost(n): # Cost to move n spaces.
    try:
        return cost_dir[n]
    except KeyError:
        res = int(n*(n+1)/2)
        cost_dir[n]=res
        return res

if __name__=="__main__":
    f = open(filename,"r")
    l = f.readline()[:-1]
    plist = eval('['+l+']')

    vlist = [0]*max(plist)

    phist = {}
    for p in plist:
        try:
            phist[p]+=1
        except KeyError:
            phist[p]=1
                    
    for (p,m) in phist.items():
        for i in range(len(vlist)):
            vlist[i]+=m*cost(abs(p-i))

    min_res = min(vlist)
    print("Minimal fuel cost: ", min_res)
    
