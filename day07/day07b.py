filename = "input.txt"

# Not thrilled with the n^2 algorithm.
# Can tinker at the margins, do a histogram of
# values first, maybe?
def cost(n): # Cost to move n spaces.
    return int(n*(n+1)/2)

if __name__=="__main__":
    f = open(filename,"r")
    l = f.readline()[:-1]
    plist = eval('['+l+']')

    vlist = [0]*max(plist)

    for p in plist:
        for i in range(len(vlist)):
            vlist[i]+=cost(abs(p-i))

    min_res = min(vlist)
    print("Minimal fuel cost: ", min_res)
    
