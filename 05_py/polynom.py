def polyEval(lst:list[float], x:float)->float:
    pol_x = 0
    while lst[len(lst)-1] == 0:
        lst.pop(len(lst)-1)
    for i in range(0, len(lst), +1):
        pol_x += lst[i]*(x**i)
    return pol_x

def polySum(lst1:list[float], lst2:list[float]):
    poly_sum = []
    while lst1[len(lst1)-1] == 0:
        lst1.pop(len(lst1)-1)
    while lst2[len(lst2)-1] == 0:
        lst2.pop(len(lst2)-1)
    if len(lst1) >= len(lst2):
        poly_sum = lst1
        for i in range(0, len(lst2), +1):
            poly_sum[i] += lst2[i]
    else:
        poly_sum = lst2
        for i in range(0, len(lst1), +1):
            poly_sum[i] += lst1[i]
    while poly_sum[len(poly_sum)-1] == 0:
        poly_sum.pop(len(poly_sum)-1)
    return poly_sum

def polyMultiply(lst1:list[float], lst2:list[float]):
    poly_mul = []
    while lst1[len(lst1)-1] == 0:
        lst1.pop(len(lst1)-1)
    while lst2[len(lst2)-1] == 0:
        lst2.pop(len(lst2)-1)
    for i in range(0, len(lst1), +1):
        for n in range(0, len(lst2), +1):
            if len(poly_mul) < i+n+1:
                poly_mul.append(lst1[i] * lst2[n])
            else:
                poly_mul[i+n] += lst1[i] * lst2[n]
    return poly_mul