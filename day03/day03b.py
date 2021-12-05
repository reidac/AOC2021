
inc = {'0':-1,'1':1}
val = {True: 1, False: 0}
dct = {}
oxy = set()
co2 = set()

nbits = 5
filename = "test.txt"

# Probably memory-inefficient, but here goes.
# Retain every element in the set whose bit at
# position bitpos (counting from left to right)
# matches the template. 
def prune(inset,bitpos,template):
    res = set()
    for s in inset:
        if int(s[bitpos])==template[bitpos]:
            res.add(s)
    return res
    
if __name__=="__main__":
    f = open(filename)
    for l in f:
        oxy.add(l[:-1])
        co2.add(l[:-1])
        for c in zip(range(nbits,0,-1),l[:-1]):
            delta = inc[c[1]]
            try:
                dct[c[0]]+=delta
            except KeyError:
                dct[c[0]]=delta

    # For bit position k-1 (MSB is 11, LSB is 0), the most common
    # bit is 1 if dct[k]>0, and zero of dct[k]<0.

    # TODO: This is wrong, you need to re-assess the most
    # common bit after each pruning operation. 
    oxy_template = [ val[ dct[k] > 0] for k in range(nbits,0,-1)]
    for pos in range(nbits):
        oxy = prune(oxy,pos,oxy_template)
        if len(oxy)==1:
            break

    co2_template = [ val[ dct[k] < 0] for k in range(nbits,0,-1)]
    for pos in range(nbits):
        co2 = prune(co2,pos,co2_template)
        if len(co2)==1:
            break

    print(oxy,co2)
        

    
            
                
            
