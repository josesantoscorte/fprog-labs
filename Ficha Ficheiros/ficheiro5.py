def procura(palavra, ficheiro):
    with open(ficheiro) as file:
        lines = file.readlines()
        for line in lines:
            if palavra in line.split(' '):
                print(line)




procura('teste', 'teste.txt')
procura('stuartmill', 'teste.txt')