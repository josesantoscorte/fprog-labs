def impares(num):
    if num == 0:
        return num
    elif (num%10) % 2 == 1:
        return num % 10 + 10*impares(num // 10)
    else:
        return impares(num // 10)

print(impares(123456789))

