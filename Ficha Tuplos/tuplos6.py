def num_para_seq_cod(num):
    res = ()
    if num <= 0:
        raise ValueError('O numero tem que ser inteiro positivo')
    num = [int(i) for i in str(num)]
    for i in range(len(num)):
        if num[i] % 2 == 0:
            res += ((num[i]+2)%10,)
        else:
            res += ((num[i]-2)%10,)
    return res

print(num_para_seq_cod(123))