def elemento_matriz(matriz, linha, coluna):
    try: return matriz[linha][coluna]
    except: raise ValueError('indice inválido')

m = [[1,2,3],[4,5,6]]
print(elemento_matriz(m, 0, 0))