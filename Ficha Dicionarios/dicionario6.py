def palavras(string):
    res = {}
    i = 0
    while i < len(string):
        while string[i] == ' ':
            i += 1
        string = ' '
        while string[i] != ' ':
            string += string[i]
            i += 1
        if string not in res: res[string] = 0



cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'

palavras(cc)