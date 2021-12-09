
filename = "input.txt"


def str_intersect(s1,s2):
    st1 = set(s1)
    st2 = set(s2)
    st3 = st1.intersection(st2)
    return ''.join(st3)
    
def resolve(in_data,out_data):
    # Input data is 10 strings, representing segment combinations,
    # output data is four digits made from the segments. The goal
    # is to ID the digits, and return the four-digit number.
    in_dict = {}
    for v in in_data:
        in_dict[ "".join(sorted(v)) ] = None
    # Step 0: Assign the obvious knowns.
    for k in in_dict.keys():
        if len(k)==2:
            one_str = k
            in_dict[k]=1
        if len(k)==3:
            seven_str = k
            in_dict[k]=7
        if len(k)==7:
            eight_str = k # Probably not useful.
            in_dict[k]=8
        if len(k)==4:
            four_str = k
            in_dict[k]=4
    # Find the '6'.
    for k in in_dict.keys():
        if len(k)==6:
            isec = str_intersect(k,one_str)
            if len(isec)==1:
                seg_f = isec
                in_dict[k]=6
    # Resolve the fives.
    for k in in_dict.keys():
        if len(k)==5:
            isec = str_intersect(k,one_str)
            if len(isec)==2:
                in_dict[k]=3
            if len(isec)==1:
                if isec==seg_f:
                    in_dict[k]=5
                else:
                    in_dict[k]=2
    # Resolve the sixes.
    for k in in_dict.keys():
        if len(k)==6:
            isec = str_intersect(k,four_str)
            if len(isec)==4:
                in_dict[k]=9
            else:
                if in_dict[k] is None:
                    in_dict[k]=0 # Don't overwrite the 6!
                
    out_data_s = [ "".join(sorted(x)) for x in out_data ]

    res = 0
    for d in out_data_s:
        res = res*10+in_dict[d]
    return res
    

if __name__=="__main__":
    f = open(filename, "r")
    res = 0
    for l in f:
        halves = l.split('|')
        input_data = halves[0].split()
        output_data = halves[-1].split()
        res += resolve(input_data,output_data)
    print("Sum of outputs: ", res)
