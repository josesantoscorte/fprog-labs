def invert(num):
    res = 0
    count = 1
    while num != 0:
        res = res + (count* (num % 10))
        num = num // 10
        count = count * 10
    return res

def explode(num):
    if type(num) != int:
        raise ValueError('Argumento não inteiro')
    else:
        res = ()
        num = invert(num)
        while num != 0:
            res += (num % 10,)
            num = num // 10
        return res
print(explode(123))

