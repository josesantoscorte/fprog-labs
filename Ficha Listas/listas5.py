def matriz_print(matriz):
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print()

m = [[1,2,3],[3,4,5],[6,7,8]]

matriz_print(m)