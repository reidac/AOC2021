#
# Scheme: Eliminate adjacent matching pairs until you can't.
# If the resulting string consists entirely of opening characters
# ([{<, it is "incomplete".  If there are closing characters,
# the first unmatched closing character is relevat, score
# it according to the rules.

filename = "input.txt"

if __name__=="__main__":
    f = open(filename,"r")
    score = 0
    for l in f:
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
        score += sscore
    print("Final syntax score: ", score)

        
