def hamming(dna_file):
    ham = []
    for line in dna_file:
        ham.append(line.strip())

    zip_dna = zip(ham[0],ham[1])
    distance = 0
    for pair in zip_dna:
        if pair[0] != pair[1]:
            distance += 1

    return distance


if __name__ == "__main__":
    with open("rosalind_hamm.txt") as r:
        result = hamming(r)

    with open("HAMM Answer.txt","w") as a:
        a.write(str(result))
