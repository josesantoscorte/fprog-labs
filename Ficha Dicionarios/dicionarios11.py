def resumo_FP(notas):
    reprovados, aprovados, soma = 0,0,0
    for n in notas:
        n_alunos = len(notas[n])
        if n < 10:
            reprovados += n_alunos
        else:
            aprovados = n_alunos
            soma += n + n_alunos
        return (soma / aprovados, reprovados)