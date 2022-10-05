from functools import reduce

def soma_fn_for(n, fn):
    soma = 0
    for x in range(0, n+1):
        soma += fn(x)
    return soma

def soma_fn(n, fn):
    def soma_fn_aux(n, fn, soma):
        if n == 0:
            return soma
        else:
            return soma_fn_aux(n-1, fn, soma + fn(n))
    return soma_fn_aux(n, fn, 0)

def filtrar(lst, tst):
    return list(filter(tst, lst))

def acumula(lst, fn):
    return reduce(lambda x, y: x + fn(y), lst)

def soma_quadrados_impares(lst):
    return reduce(lambda soma, x: soma + x**2 if x % 2 != 0 else soma, lst)

def digitos(lst):
    return list(map(lambda x: int(x), str(lst)))

print(digitos(12345))