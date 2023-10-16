def je_prvocislo(n: int)->bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(je_prvocislo(11))