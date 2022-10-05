from listas5 import matriz_print

def soma_mat(m1, m2):
    res = []
    for i in m1:
        for j in i:
            res.append(m1[i, j] + m2[i, j])
    return res

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]

matriz_print(soma_mat(m1, m2))