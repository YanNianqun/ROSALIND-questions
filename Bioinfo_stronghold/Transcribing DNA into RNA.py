import sys
with open (sys.argv[1], 'r') as f:
    for line in f:
        line=line.upper()
        line = list(line.rstrip())
        for i in range(len(line)):
            if line[i] == 'T':
                line[i] = 'U'
        '''This also work
        for i in line:
            if i == 'T':
                i = 'U'
        '''
            print(line[i],end='')
