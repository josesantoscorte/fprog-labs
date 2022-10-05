def conta_vogais(nome):
    vogais = ('a', 'e', 'i', 'o', 'u')
    count = 0
    file = open(nome) 
    for line in file:
        for char in line:
            if char in vogais:
                count += 1
    file.close()
    return count

print(conta_vogais('teste.txt'))