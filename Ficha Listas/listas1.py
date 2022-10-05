def lista_codigos(string):
    res = []
    for i in string:
        res.append(ord(i))
    return res

print(lista_codigos('bom dia'))
