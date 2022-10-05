#123
#241
#542

def invert(num):
    last = num % 10
    mid = (num // 10) % 10
    first = (num // 100) % 10
    if first - last > 1:
        return last*100 + mid*10 + first
    else:
        return -1

def misterio(num):
    if (invert(num) != -1):
        num_s = abs(num - invert(num))
        last = num_s % 10
        mid = (num_s // 10) % 10
        first = (num_s // 100) % 10
        num_si = last*100 + mid*10 + first
        print(num_s + num_si)
    else:
        print('A difrença entre o primeiro e o ultimo digito é <= 1')

misterio(642)
misterio(131)
