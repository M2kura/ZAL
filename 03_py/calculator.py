import math

def addition(x, y):
    while type(x) != str and type(y) != str:
        sum = x + y
        return sum
    else:
        ValueError('This operation is not supported for given input parameters')

def subtraction(x, y):
    if x != str and y != str:
        sum = x - y
        return sum
    else:
        ValueError('This operation is not supported for given input parameters')

def multiplication(x, y):
    if x != str and y != str:
        sum = x * y
        return sum
    else:
        ValueError('This operation is not supported for given input parameters')

def division(x, y):
    if x != str and y != str and y != 0:
        sum = x / y
        return sum
    else:
        ValueError('This operation is not supported for given input parameters')

def modulo(x, y):
    if x != str and y != str and x >= y and y > 0:
        sum = x % y
        return sum
    else: 
        raise ValueError('This operation is not supported for given input parameters')

def secondPower(x):
    if x != str:
        sum = x ** 2
        return sum
    else:
        raise ValueError('This operation is not supported for given input parameters')

def power(x, y):
    if x != str and y != str and y >= 0:
        sum = float(x ** y)
        return sum
    else: 
        raise ValueError('This operation is not supported for given input parameters')

def secondRadix(x):
    if x != str and x > 0:
        sum = math.sqrt(x)
        return sum
    else:
        raise ValueError('This operation is not supported for given input parameters')

def magic(x, y, z, k):
    if x != str and y != str and z != str and k != str and m != 0:
        l = x + k
        m = y + z
        n = ((l/m)+1)
        return n

def control(a, x, y, z, k):
    while x != str and y != str and z != str and k != str:
        if a == 'ADDITION':
            return addition(x, y)
        elif a == 'SUBTRACTION':
            return subtraction(x, y)
        elif a == 'MULTIPLICATION':
            return multiplication(x, y)
        elif a == 'DIVISION':
            sum = division(x, y)
            return sum
        elif a == 'MOD':
            sum = modulo(x, y)
            return sum
        elif a == 'POWER':
            sum = power(x, y)
            return sum
        elif a == 'SECONDRADIX':
            sum = subtraction(x)
            return sum
        elif a == 'MAGIC':
            sum = magic(x, y, z, k)
            return sum
        else:
            raise ValueError('This operation is not supported for given input parameters')
    else:
        raise ValueError('This operation is not supported for given input parameters')
    
print(addition(4, "2"))