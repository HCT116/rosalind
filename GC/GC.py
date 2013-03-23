import string

def read_fasta(f):
    fasta_dict = {}
    ugly_split = f.strip(">").split(">") #separates sequences ugly
    for split in ugly_split:
        split2 = split.strip().split() #splits by whitespace 
        fasta_dict[split2[0]] = "".join(split2[1:])
    return fasta_dict

def gc_content(dna_dict):
    highest = ["",0]
    for key,value in dna_dict.iteritems():
        gcpercent = (value.count("G") + value.count("C"))/float(len(value))*100.0
        if gcpercent > highest[1]:
            highest = [key,gcpercent]
    best = "{0}\n{1}".format(highest[0],highest[1])
    return best

if __name__ == "__main__":
    with open("rosalind_gc.txt") as r:
        raw_file = r.read()

    dna_seqs = read_fasta(raw_file)
    result = gc_content(dna_seqs)

    with open("GC Answer.txt","w") as a:
        a.write(result)
