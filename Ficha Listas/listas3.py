def soma_cumultativa(lista):
    res = []
    soma = 0
    for i in lista:
        res.append(i+soma)
        soma += i
    return res

print(soma_cumultativa([1,2,3,4,5]))

