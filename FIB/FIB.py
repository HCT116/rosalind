def wabbits(mos,litter,newborn,gestating,reproducing):
    reproducing += newborn#newborns mature to reproducing age
    newborn = gestating #babies are born into newborns
    gestating = reproducing*litter #reproducing act makes fetuses
    mos -= 1
    if mos == 1:
        return reproducing + newborn
    return wabbits(mos,litter,newborn,gestating,reproducing)

if __name__ == "__main__":
    with open("rosalind_fib.txt") as r:
        n_str, k_str = r.read().strip().split()
        n, k = int(n_str), int(k_str)

    result = wabbits(n,k,1,0,0)

    with open("FIB Answer.txt","w") as a:
        a.write(str(result))
