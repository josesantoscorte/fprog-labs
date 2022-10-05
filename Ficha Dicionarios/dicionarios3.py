def baralho():
    res = []
    for np in ('esp','cop','our','cor'):
        for v in '123456789','10','JQKA':
            res.append({'np': np, 'vlr': v})
    return res

print(baralho())