if __name__ == "__main__":
    with open("rosalind_iev.txt") as r:
        probs_lst = zip([1,1,1,0.75,0.5,0],[int(x) for x in r.read().split()])
        result = int(sum((2*x*y for x,y in probs_lst)))

    with open("IEV Answer.txt","w") as a:
        a.write(str(result))
