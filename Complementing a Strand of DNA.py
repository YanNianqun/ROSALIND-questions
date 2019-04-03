import sys
with open (sys.argv[1], 'r') as f:
    for line in f:
        line=line.upper()
        line = list(line.rstrip())
        line =line[::-1]
        for i in range(len(line)):
            if line[i] == 'A':
                line[i] = 'T'
            elif line[i] == 'T':
                line[i] = 'A'
            elif line[i] == 'G':
                line[i] = 'C'
            elif line[i] == 'C':
                line[i] = 'G'
            print(line[i],end='')
