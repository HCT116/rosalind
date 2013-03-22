def count(seq):
    a,t,c,g=0,0,0,0
    for base in seq:
        if base == 'A':
            a+=1
        elif base == 'T':
            t+=1
        elif base == 'C':
            c+=1
        elif base == 'G':
            g+=1
    print a,c,g,t
