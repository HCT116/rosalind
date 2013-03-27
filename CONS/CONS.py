#clean up with numpy arrays! loops are messy

def read_fasta(file_str):
    fasta_dict = {}
    ugly_split = file_str.strip(">").split(">") #separates sequences ugly
    for split in ugly_split:
        split2 = split.strip().split() #splits by whitespace 
        fasta_dict[split2[0]] = "".join(split2[1:])
    return fasta_dict

def profile_matrix(dna_dict):
    dna_list = []
    for _, dna in dna_dict.iteritems():
        dna_list.append([i for i in dna])

    consensus_list=[]
    for base in 'ACGT':
        a = []
        for index in xrange(len(dna_list[0])):
            a.append([i[index] for i in dna_list].count(base))
        consensus_list.append(a)

    return consensus_list

def consensus_string(matrix):
    cons_str = ""
    for index in xrange(len(matrix[0])):
        matrix_col = [i[index] for i in matrix] #column of matrix as list
        max_i = matrix_col.index(max(matrix_col)) #index of most base

        if max_i == 0:
            cons_str += 'A'
        elif max_i == 1:
            cons_str += 'C'
        elif max_i == 2:
            cons_str += 'G'
        elif max_i == 3:
            cons_str += 'T'
    return cons_str

if __name__ == "__main__":
    with open("rosalind_cons.txt") as r:
        seq_dict = read_fasta(r.read())
        mat = profile_matrix(seq_dict)
        cons = consensus_string(mat)
        matA = 'A: ' + " ".join([str(i) for i in mat[0]]) + '\n'
        matC = 'C: ' + " ".join([str(i) for i in mat[1]]) + '\n'
        matG = 'G: ' + " ".join([str(i) for i in mat[2]]) + '\n'
        matT = 'T: ' + " ".join([str(i) for i in mat[3]])
        result = cons + '\n' + matA + matC + matG + matT


    with open("CONS Answer.txt","w") as a:
        pass
        a.write(result)
