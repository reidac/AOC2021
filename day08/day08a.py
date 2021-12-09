
filename = "input.txt"

if __name__=="__main__":
    f = open(filename, "r")
    count = 0
    for l in f:
        output_half = l.split('|')[-1]
        output_data = output_half.split()
        for v in output_data:
            if len(v)==2 or len(v)==3 or len(v)==4 or len(v)==7:
                count += 1
    print("Number of 1,7,4,8 instances in output: ",count)
