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
    y = 0
    for i in range(1, x+1):
        if i % 2 == 1:
            y+=(4/(i+i-1))
        else:
            y+=(-(4/(i+i-1)))
    return y
    
def nilakanthaPi(n: int):
    sum = 3
    if n == 1:
        return sum
    else:
        for i in range(2, n+1):
            z = i*2
            if i % 2 == 0:
                x = 4/(z*(z-1)*(z-2))
            else:
                x = -(4/(z*(z-1)*(z-2)))
            sum += x
    return sum