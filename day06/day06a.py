

filename = "input.txt"
daycount = 80

if __name__=="__main__":
    f = open(filename,'r')
    l = f.readline()[:-1]
    lst = eval('['+l+']')

    for d in range(daycount):
        newbies = []
        for i in range(len(lst)):
            if lst[i]==0:
                lst[i]=6
                newbies.append(8)
            else:
                lst[i]-=1
        lst += newbies
    print("Number of fishies: ", len(lst))
    
