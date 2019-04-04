import sys
with open(sys.argv[1],'r') as f:
    Seqlist=[]
    for line in f:
        line=line.rstrip()
        Seqlist.append(line)
    HammingDis=0
    # Seqlist[1]='AG'.If not use try, when first seq shorter than the second one, IndexError happen.
    #index out of range
    try:
        for i in range(len(Seqlist[0])):
            if Seqlist[0][i] != Seqlist[1][i]:
                HammingDis += 1
    except:
        print(HammingDis)
    else:
        print(Seqlist)
        print(HammingDis)
