#
# Scheme: Eliminate adjacent matching pairs until you can't.
# If the resulting string consists entirely of opening characters
# ([{<, it is "incomplete".  If there are closing characters,
# the first unmatched closing character is relevat, score
# it according to the rules.

filename = "input.txt"
# filename = "test.txt"

if __name__=="__main__":
    f = open(filename,"r")
    cscore_list = []
    for l in f:
        # assert(l[-1]=='\n')
        s = l[:-1] # Remove trailing newline.
        # Prune all the matching pairs.
        sl = len(s)
        done = False
        while not done:
            s = s.replace("<>","")
            s = s.replace("[]","")
            s = s.replace("()","")
            s = s.replace("{}","")
            nsl = len(s)
            if nsl==sl: # No change...
                done = True
            else:
                sl = nsl
        # Find the first closing item and score it.
        min_idx = None
        sscore = 0
        scoremap = { ')':3, ']':57, '}':1197, '>':25137}
        for (c,v) in scoremap.items():
            try:
                idx = s.index(c)
            except ValueError:
                pass
            else:
                if (min_idx is None) or (idx < min_idx):
                    min_idx = idx
                    sscore = v
        # Now sscore is 0 if no match was ever found, or the map score.
        if (sscore==0):
            cscore = 0
            cmap = {'(':1, '[':2, '{':3, '<':4 }
            for c in s[::-1]:
                cscore = cscore*5+cmap[c]
            cscore_list.append(cscore)
    cscore_list.sort()
    print("Middle completion score: ",cscore_list[len(cscore_list)//2])
    
