
inc = {'0':-1,'1':1}
dct = {}

if __name__=="__main__":
    f = open("input.txt")
    for l in f:
        for c in zip(range(12,0,-1),l[:-1]):
            delta = inc[c[1]]
            try:
                dct[c[0]]+=delta
            except KeyError:
                dct[c[0]]=delta

    gamma = 0
    epsilon = 0
    for (k,v) in dct.items():
        if (v>0):
            gamma += (2**(k-1))
        elif (v<0):
            epsilon += (2**(k-1))
        else:
            print("Oops!")

    print("Product: ",gamma*epsilon)
            

    
            
                
            
