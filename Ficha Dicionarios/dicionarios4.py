def metabolismo(px):
    res = {}
    for p in px:
        if px[p][0] == 'M':
            res[p] = 66 + 6.3 * px[p][3] #...
        else:
            res[p] = 66 #...
    return res