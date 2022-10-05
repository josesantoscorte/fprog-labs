def ordena_ficheiro(entrada):
    with open(entrada, 'r') as entrada:
        lines = sorted(entrada.readlines())
        for line in lines:
            print(line)
    

ordena_ficheiro('teste.txt')