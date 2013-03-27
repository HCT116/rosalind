def wabbits(mos,alivemos,L=None):
    #gonna use a list of 3 tuples of gestating,newborn,reproducing numbers
    if L is None:#first month
        L=[]
        gestating,newborn,reproducing = 0, 1, 0
        L.append((gestating,newborn,reproducing))
        
    else:
        gestating,newborn,reproducing = L[-1][0], L[-1][1], L[-1][2]

        if len(L) >= alivemos:#old ones who where newborn alivemos ago die
            reproducing -= L[-alivemos][1]

        reproducing += newborn#newborns mature to reproducing age
        newborn = gestating #babies are born into newborns
        gestating = reproducing #reproducing act makes fetuses
        L.append((gestating,newborn,reproducing))
    
    if len(L) == mos:
        return reproducing + newborn
    return wabbits(mos,alivemos,L)

if __name__ == "__main__":
    with open("rosalind_fibd.txt") as r:
        n_str, k_str = r.read().strip().split()
        n, m = int(n_str), int(k_str)

    result = wabbits(n,m)

    with open("FIBD Answer.txt","w") as a:
        a.write(str(result))
