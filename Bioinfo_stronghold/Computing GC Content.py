import sys
with open(sys.argv[1],'r') as f:
    idl=[]
    GCL=[]
    id_n=0
    GC_n=0
    for line in f:
        if line.startswith('>'):
            seq=''
            id = line[1:].rstrip()
            idl.append(id)
            GCL.append(0)
            id_gc = idl.index(id)

            id_n += 1
        else:
            line=line.upper()
            line=line.rstrip()
            seq += line
            s = len(seq)
            gn = seq.count('G')
            cn = seq.count('C')
            GC_c = (gn+cn)/s
            GCL[id_gc]=GC_c
    GC_max=max(GCL)
    Id_need = GCL.index(GC_max)
    #print(idl,GCL)

    print(idl[Id_need],GCL[Id_need]*100)
    #pay attention to the format of the answer.
