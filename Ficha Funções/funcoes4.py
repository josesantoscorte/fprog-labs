from funcoes3 import area_circulo

def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError('r1 > r2')
    return (area_circulo(r2) - area_circulo(r1))

print(str(area_circulo(2)) + ', ' + str(area_circulo(4)))
print(area_coroa(2, 4))