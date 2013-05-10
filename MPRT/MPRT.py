import urllib2

def grab_prot_seq(prot_id):
    '''Uses a UniProt ID and returns the protein sequence thru web query'''
    address = "http://www.uniprot.org/uniprot/{0}.fasta".format(prot_id)
    try:
        u = urllib2.urlopen(address)
        fast_lst = u.read().strip().split('\n')
    finally:
        u.close()

    seq = "".join(fast_lst[1:])
    print seq
    return seq

def n_glycosylation_mot(sequence):
    '''Takes a string of amino acids and returns list of indices in str form'''
    index_lst = []
    for i in range(len(sequence)-3):
        tet = sequence[i:i+4]
        b_lst = []
        if tet[0]=="N" and ("P" not in tet[1]+tet[3]) and (tet[2] in "ST"):
            index_lst.append(str(i+1))

    return index_lst

if __name__ == "__main__":
    with open("rosalind_mprt.txt") as r:
        prots = r.read().strip().split()
        prot_list = []
        for p in prots:
            prot_list.append((p,grab_prot_seq(p)))

        r_list=[]
        for p_id, sq in prot_list:
            mot_matches = n_glycosylation_mot(sq)
            if len(mot_matches) != 0:
                r_list.append(p_id)
                r_list.append(" ".join(mot_matches))

        result = "\n".join(r_list)

    with open("MPRT Answer.txt","w") as a:
        a.write(result)
