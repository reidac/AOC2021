
inc = {'0':-1,'1':1}
val = {True: '1', False: '0'}
oxy = set()
co2 = set()

nbits = 12
filename = "input.txt"

# Probably memory-inefficient, but here goes.
# Retain every element in the set whose bit at
# position bitpos (counting from left to right)
# matches the template. 
def prune(inset,bitpos,sense):
    mci = 0 # Most common indicator
    for s in inset:
        mci += inc[s[bitpos]]
    res = set()
    for s in inset:
        if sense=='+':
            if val[mci>=0]==s[bitpos]:
                res.add(s)
        elif sense=='-':
            if val[mci>=0]!=s[bitpos]:
                res.add(s)
    return res
    
if __name__=="__main__":
    f = open(filename)
    for l in f:
        oxy.add(l[:-1])
        co2.add(l[:-1])

    for pos in range(nbits):
        oxy = prune(oxy,pos,'+')
        if len(oxy)==1:
            break

    for pos in range(nbits):
        co2 = prune(co2,pos,'-')
        if len(co2)==1:
            break

    # Can't index into sets, but they're unary, so
    # iteration is cheap.
    for so in oxy:
        vo = int(so,2)
        for sc in co2:
            vc = int(sc,2)
            print("Product: ",vo*vc)

    
            
                
            
