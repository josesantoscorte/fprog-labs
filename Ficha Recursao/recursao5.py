def soma_els_atomicos(tuplo):
    if tuplo == ():
        return 0
    elif type(tuplo[0]) == tuple:
        return soma_els_atomicos(tuplo[0]) + soma_els_atomicos(tuplo[1:])
    else:
        return tuplo[0] + soma_els_atomicos(tuplo[1:])

print(soma_els_atomicos((3, ((((((6, (7, ))), ), ), ), ), 2, 1)))