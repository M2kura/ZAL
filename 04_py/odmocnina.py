def odmocni(a: float)-> float:
    x = a
    while True:
        x_dal = 0.5 * (x + a/x)
        if x == x_dal:
            return x
        x = x_dal
print(odmocni(43))