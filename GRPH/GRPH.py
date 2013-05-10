import itertools

def read_fasta(file_str):
    fasta_dict = {}
    ugly_split = file_str.strip(">").split(">") #separates sequences ugly
    for split in ugly_split:
        split2 = split.strip().split() #splits by whitespace 
        fasta_dict[split2[0]] = "".join(split2[1:])
    return fasta_dict

def o3_adj_list(seq_dict):
    adj_list = []
    fun = itertools.permutations(seq_dict.iteritems(),2)
    for seq1, seq2 in fun:
        if seq1[1][-3:] == seq2[1][:3]:
            adj_list.append(seq1[0]+" "+seq2[0])

    return adj_list
                
if __name__ == "__main__":
    with open("rosalind_grph.txt") as r:
        seqs = read_fasta(r.read())
        o3_list = o3_adj_list(seqs)
        result = "\n".join(o3_list)

    with open("GRPH Answer.txt","w") as a:
        a.write(result)
