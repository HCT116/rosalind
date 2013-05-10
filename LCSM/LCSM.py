#SLOW!!!
def read_fasta(file_str):
    fasta_dict = {}
    ugly_split = file_str.strip(">").split(">") #separates sequences ugly
    for split in ugly_split:
        split2 = split.strip().split() #splits by whitespace 
        fasta_dict[split2[0]] = "".join(split2[1:])
    return fasta_dict

def split_x(seq, x):
    #splits string into list seqs with overlap of x-1
    split_lst = []
    for i in range(len(seq)-x+1):
        split_lst.append(seq[i:i+x])

    return split_lst
    
def longest_motif(seqs):
    match_lst = []
    for x in range(2,len(seqs[0])):
        print x
        for sub in split_x(seqs[0],x):
            if len([False for s in seqs if sub not in s]) == 0:
                match_lst.append(sub)
        if len(match_lst[-1]) != x:
            break

    return match_lst[-1]

if __name__ == "__main__":
    with open("rosalind_lcsm.txt") as r:
        seq = r.read()
        seq_list = read_fasta(seq).values()
        result = longest_motif(seq_list)

    with open("LCSM Answer.txt","w") as a:
        a.write(result)
