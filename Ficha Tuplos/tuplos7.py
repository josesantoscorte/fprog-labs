def amigas(p1, p2):
    if len(p1) != len(p2):
        raise ValueError('As palavras não são do mesmo tamanho')
    count = 0
    for i in range(len(p1)):
        if p1[i] == p2[i]:
            count += 1
    if count / len(p1) > 0.10:
        return True
    else:
        return False

print(amigas('teste', 'olart'))