import math

def addition(x, y):
    try:
        sum = float(x) + float(y)
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return sum

def subtraction(x, y):
    try:
        sum = float(x) - float(y)
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return sum

def multiplication(x, y):
    try:
        sum = float(x) * float(y)
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return sum

def division(x, y):
    try:
        sum = float(x) / float(y)
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return sum

def modulo(x, y):
    try:
        sum = float(x) % float(y)
    except: 
        raise ValueError('This operation is not supported for given input parameters')
    else:
        if float(x) >= float(y) and float(y) > 0:
            return sum
        else: 
            raise ValueError('This operation is not supported for given input parameters')

def secondPower(x):
    try:
        sum = float(x) ** 2
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return sum

def power(x, y):
    try:
        sum = float(x) ** float(y)
    except: 
        raise ValueError('This operation is not supported for given input parameters')
    else:
        if float(y) >= 0:
            return sum 
        else:
            raise ValueError('This operation is not supported for given input parameters')
            

def secondRadix(x):
    try:
        sum = math.sqrt(int(x))
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        if int(x) > 0:
            return sum
        else: 
            raise ValueError('This operation is not supported for given input parameters')


def magic(x, y, z, k):
    try:
        l = float(x) + float(k)
        m = float(y) + float(z)
        n = ((l/m)+1)
    except:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        return n

def control(a, x, y, z, k):
    if a == 'ADDITION':
        z = k = ''
        return addition(x, y)
    elif a == 'SUBTRACTION':
        z = k = ''
        return subtraction(x, y)
    elif a == 'MULTIPLICATION':
        z = k = ''
        return multiplication(x, y)
    elif a == 'DIVISION':
        z = k = ''
        return division(x, y)
    elif a == 'MOD':
        z = k = ''
        return modulo(x, y)
    elif a == 'POWER':
        z = k = ''
        return power(x, y)
    elif a == 'SECONDRADIX':
        z = k = y = ''
        return subtraction(x)
    elif a == 'MAGIC':
        return magic(x, y, z, k)
    else:
        raise ValueError('This operation is not supported for given input parameters')
    
# print(power(input("Choose a number: "), input("Choose another one: ")))
# print(secondRadix(input("Choose a number: ")))
# x = input("---> ")
# print(type(x))
# print(magic(input("1 number: "), input("2 number: "), input("3 number: "), input("4 number: ")))
# print(control('MOD', 40, input("samk"),4,5))