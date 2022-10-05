def sublistas(lista):
    if lista == []:
        return 0
    elif type(lista[0]) == list:
        return 1 + sublistas(lista[1:]) + sublistas(lista[0])
    else:
        return sublistas(lista[1:])

print(sublistas(['a', [2, 3, [[[1]], 6, 7], 'b']]))