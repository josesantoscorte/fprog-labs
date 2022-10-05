def agrupa_por_chave(pares):
    dicionario = {}
    for i in pares:
        if not i[0] in dicionario:
            dicionario[i[0]] = []
        dicionario[i[0]].append(i[1])
    return dicionario

lista = [('a',8),('b',9),('a',3)]
print(agrupa_por_chave(lista))