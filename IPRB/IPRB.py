def dom_prob(DD,Dd,dd):
    n = sum([DD,Dd,dd])

    DDstart = DD/n*1
    Ddstart = Dd/n*(1*DD/(n-1)+0.75*(Dd-1)/(n-1)+0.5*dd/(n-1))
    ddstart = dd/n*(1*DD/(n-1)+0.5*Dd/(n-1)+0*(dd-1)/(n-1))

    return (DDstart+Ddstart+ddstart)
    
if __name__ == "__main__":
    with open("rosalind_iprb.txt") as r:
       dom, het, rec  = [float(i) for i in r.read().split()]
       result = dom_prob(dom, het, rec)

    with open("IPRB Answer.txt","w") as a:
        a.write(str(result))
