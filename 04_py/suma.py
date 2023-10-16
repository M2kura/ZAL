def suma(min:float, max:float)->float:
    sum = 0
    for i in range(min, max+1):
        sum+=i
    return sum

print(suma(1,10))