def conta_linhas(string):
    ficheiro = open(string, 'r')
    count = 0
    for line in ficheiro:
        if line != '\n':
            count += 1
    return count

print(conta_linhas('teste.txt'))

