import sys
with open (sys.argv[1],'r') as f:
    Na=0
    Nt=0
    Nc=0
    Ng=0
    for line in f:
        line=line.upper()
        for i in line:
            if i == 'A':
                Na += 1
            elif i == 'T':
                Nt += 1
            elif i == "G":
                Ng += 1
            elif i == "C": #we can also use string.count()
                Nc += 1
    print(Na,Nc, Ng, Nt)
