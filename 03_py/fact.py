def fakt(initial):
    res = 1
    for i in range(initial,1 , -1):
        res *= i
    return res

def fakt1(initial):
    res = 1
    i = initial
    while i > 1:
        res *= i
        i -= 1
    return res


# print(fakt(4))
print(list(range(4, 1, -1)))