def newtonPi(init):
    pass


def leibnizPi(x: int):
    pilist = []
    for i in range(1, x+1):
        if i % 2 == 1:
            pilist.append(4/(i+i-1))
        else:
            pilist.append(-(4/(i+i-1)))
    return sum(pilist)
    




def nilakanthaPi(iterations):
    pass