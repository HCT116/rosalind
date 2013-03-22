with open("rosalind_revc.txt") as r:
    seq = r.read()

seq=seq[::-1]
seq=seq.replace("A","t",seq.count("A"))
seq=seq.replace("T","a",seq.count("T"))
seq=seq.replace("C","g",seq.count("C"))
seq=seq.replace("G","c",seq.count("G"))
seq=seq.upper()

with open("REVC Answer.txt","wb") as a:
    a.write(seq)
