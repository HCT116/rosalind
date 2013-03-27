if __name__ == "__main__":
    with open("rosalind_subs.txt") as r:
        seq, sub = r.read().split()
        result_list = [str(i+1) for i in xrange(len(seq)-len(sub)) if seq[i:i+len(sub)] == sub]
        result = " ".join(result_list)
        

    with open("SUBS Answer.txt","w") as a:
        a.write(result)
