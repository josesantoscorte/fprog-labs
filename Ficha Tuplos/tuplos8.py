def junta_ordenados(t1, t2):
    res = ()
    i, j = 0, 0
    while  i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            res += (t1[i],)
            i += 1
        else:
            res += (t1[j],)
            j += 1    
    return res + t1[i:] + t2[j:]


print(junta_ordenados((2, 34, 200, 210), (1, 23)))