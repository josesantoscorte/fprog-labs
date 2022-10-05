def remove_multiplos(lista, inteiro):
    res = []
    for i in lista:
        if i % inteiro != 0:
            res.append(i)
    return res

print(remove_multiplos([2,3,5,9,12,33,34,45], 3))