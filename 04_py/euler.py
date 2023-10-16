def fakt(initial):
    res = 1
    for i in range(initial, 1 , -1):
        res *= i
    return res

def euler(max_iter: int)->float:
    result=0
    for i in range(max_iter):
        result+=1/fakt(i)
    return result

print(euler(400))