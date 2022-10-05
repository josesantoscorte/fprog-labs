def criar_rac(n, d):
    if type(n) != int or type(d) != int or d < 0:
        raise ValueError('Argumentos Inválidos')
    return {'n': n, 'd': d}

def num_rac(rac):
    return rac['n']

def den_rac(rac):
    return rac['d']

def eh_rac(rac):
    if type(rac) != dict or len(rac) != 2 or 'n' not in rac.keys() or 'd' not in rac.keys():
        return False
    return True

def eh_rac_zero(rac):
    if eh_rac(rac) and rac['n'] == 0:
        return True
    return False

def rac_iguais(rac1, rac2):
    if eh_rac(rac1) and eh_rac(rac2) and (rac1['n'] * rac2['d'] == rac2['n'] * rac1['d']):
        return True
    return False

def rac_print(rac):
    if not eh_rac(rac):
        raise ValueError('Argumento Inválido')
    return f'{num_rac(rac)}/{den_rac(rac)}'

def rac_prod(rac1, rac2):
    if not eh_rac(rac1) and not eh_rac(rac2):
        raise ValueError
    num = num_rac(rac1) * num_rac(rac2)
    den = den_rac(rac1) * den_rac(rac2)
    return criar_rac(num, den)

rac1 = criar_rac(1, 2)
rac2 = criar_rac(3, 4)

print(rac_print(rac_prod(rac1, rac2)))