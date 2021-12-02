import string

if __name__=="__main__":
    depth = 0
    dist = 0
    f = open("input.txt","r")
    for l in f:
        tks = l[:-1].split()
        if (tks[0]=='forward'):
            dist += int(tks[1])
        elif (tks[0]=='down'):
            depth += int(tks[1])
        elif (tks[0]=='up'):
            depth -= int(tks[1])

    res = depth*dist
    print("Product: ", res)
        
