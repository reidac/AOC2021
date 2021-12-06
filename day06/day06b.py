

filename = "input.txt"
daycount = 256

# How many fish result from a single fish with a timer
# of n after d days?

fishdict = {}

# The "fishcount" function counts how many fish result
# from a single fish with a timer of n after d days.
# Uses "fishdict" to record results to avoid having
# to re-do work.
def fishcount(n,d):
    try:
        return fishdict[(n,d)]
    except KeyError:
        if (d<=n):
            res = 1
            fishdict[(n,d)] = res
            return res
        else:
            res = fishcount(6,d-(n+1))+fishcount(8,d-(n+1))
            fishdict[(n,d)] = res
            return res
    
if __name__=="__main__":
    f = open(filename,'r')
    l = f.readline()[:-1]
    lst = eval('['+l+']')

    cdict = {}
    for v in lst:
        try:
            cdict[v] += 1
        except KeyError:
            cdict[v] = 1

    sum = 0
    for (v,m) in cdict.items():
        fc = fishcount(v,256)
        sum += fc*m
            
    print("Number of fishies: ", sum)

    
