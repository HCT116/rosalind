import re

codons = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G""".strip().split()

codon_dict = dict(zip(codons[::2],codons[1::2]))

def translate(dna):
    '''Takes a DNA string and translates into an RNA string'''
    trans_dict = dict(zip(["A","T","C","G"],["U","A","G","C"]))
    rna = ""
    for b in dna:
        rna += trans_dict[b]

    return rna

def transcribe(rna):
    """Takes an rna string and returns AAs in string useful for this problem"""
    prot = []
    for i in range(len(rna)-2):
        prot.append(codon_dict[b[i:i+3]])

    return "".join(prot)

if __name__ == "__main__":
    with open("rosalind_orf.txt") as r:
        seq = r.read().strip()

    aa_list = transcribe(translate(seq))
    re.compile('M.+?(?:Stop)')

    with open("ORF Answer.txt","w") as a:
        a.write(result)
