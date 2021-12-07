

filename = "input.txt"
daycount = 256

# More clever algorithm that just manipulates a small
# state vector.  For every tick, fishies decrement
# their timers, which moves them towards a lower
# index in the list, except fishes at 0 go 
# to index 6, and spanw new fishies at index 8.

# A possibly even more clever thing is to make this
# a matrix operation, which would allow larger
# "strides" by using powers of the resulting
# matrix.
def tick(lst): 
    res = lst[1:]+[lst[0]]
    res[6]+=lst[0]
    return res
    
if __name__=="__main__":
    f = open(filename,'r')
    l = f.readline()[:-1]
    fish_lst = eval('['+l+']')

    state = [0]*9 # Indexable up to 8.

    for v in fish_lst:
        state[v]+=1
            
    for i in range(80):
        state = tick(state)
    print("Part 1: ", sum(state))
    for i in range(daycount-80):
        state = tick(state)
    print("Part 2: ", sum(state))
    print("Final state vector: ", state)
