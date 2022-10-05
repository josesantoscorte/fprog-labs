def parte(lista, num):
    def parte_aux(lista, maiores, menores):
        if lista == []:
            return [maiores, menores]
        elif lista[0] < num:
            return parte_aux(lista[1:], maiores, [lista[0]]) + menores 
        else:
            return parte_aux(lista[1: ], menores, [lista[0])
    return parte_aux(lista, [], [])

print(parte([3, 5, 1, 4, 5, 8, 9], 4))