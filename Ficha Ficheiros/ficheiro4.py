def concatena(lista, saida):
    with open(saida, 'a') as saida:
        for ficheiro in lista:
            with open(ficheiro, 'r') as file:
                for line in file:
                    saida.write(line)


ficheiros = ['teste.txt', 'segundo.txt']

concatena(ficheiros, 'saida.txt')