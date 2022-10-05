def soma(a, b, n):
    if n == 0:
        return b
    else:
        return a + soma(a, b, n - 1)


print(soma(3, 2, 5))