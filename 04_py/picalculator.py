import math
import itertools

def newtonPi(x):
    y = x - (math.sin(x)/math.cos(x))
    list = [y]
    if y != 0:
        for i in itertools.count(start=1, step=1):
            list.append(list[i-1] - (math.sin(list[i-1])/math.cos(list[i-1])))
            while list[i] != list[i-1]:
                break
            else:
                return list[i]
    else:
        return x


def leibnizPi(x: int):
    pilist = []
    for i in range(1, x+1):
        if i % 2 == 1:
            pilist.append(4/(i+i-1))
        else:
            pilist.append(-(4/(i+i-1)))
    return sum(pilist)
        
def nilakanthaPi(x: int):
    y = 3
    pilist = []
    if x == 1:
        return y
    else:
        for i in range(2, x+1):
            z = i*2
            if i % 2 == 0:
                pilist.append(4/(z*(z-1)*(z-2)))
            else:
                pilist.append(-(4/(z*(z-1)*(z-2))))
    return y+sum(pilist)