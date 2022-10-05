def junta(lista1, lista2):
    if lista1 == [] and lista2 == []:
        return lista1 + lista2
    elif lista1[0] < lista2[0]:
        return [lista1[0]] + junta(lista1[1:], lista2)
    else:
        return [lista2[0]] + junta(lista2[1:], lista1)
        
junta([1,2],[3,4])