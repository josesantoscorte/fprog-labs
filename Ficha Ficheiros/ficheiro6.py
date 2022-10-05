def corta(entrada, saida, num):
    with open(entrada, 'r') as entrada:
        with open(saida, 'w') as saida:
            for line in entrada.readlines():
                for char in line:
                    saida.write(char)
                    num -= 1
                    if num == 0: return 'done'

corta('teste.txt', 'saida.txt', 6)


