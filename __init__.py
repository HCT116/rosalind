def read_fasta(file_str):
    fasta_dict = {}
    ugly_split = file_str.strip(">").split(">") #separates sequences ugly
    for split in ugly_split:
        split2 = split.strip().split() #splits by whitespace 
        fasta_dict[split2[0]] = "".join(split2[1:])
    return fasta_dict
