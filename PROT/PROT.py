#after reading an elegant solution could just loop through string with range
#Forgot to use dict
#I had originally made a list with append but changed to string += after
#looking at solution. Memory inefficient now (mine might have been better?)
with open("PROT RNA codons.txt","rb") as c_file:
    codon_dict = {} #dict where key is codon and value is amino acid or stop
    for line in c_file:
        spltln = line.split()
        print spltln
        codon_lst = spltln[::2]
        aa_lst = spltln[1::2]
        combined = zip(codon_lst,aa_lst)#dict() does the same as the next 2 lns
        for pair in combined:
            codon_dict[pair[0]] = pair[1]

with open("rosalind_prot.txt") as r:
    seq = r.read()
    codon_seq = zip(seq[::3],seq[1::3],seq[2::3])#makes list of 3-tuples of codons
    polypep = ""
    for codon_tup in codon_seq:
        codon_str = "".join(codon_tup)
        aa = codon_dict[codon_str]
        if aa != "Stop":
            polypep += aa
        else:
            break

with open("PROT Answer.txt","w") as a:
    a.write(polypep)
