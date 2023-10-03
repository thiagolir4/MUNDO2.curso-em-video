v1 = float(input('Digite aqui um valor: '))
v2 = float(input('Digite outro valor: '))

if v1 > v2:
    print('O \033[32m{:.2f}\033[m é maior do que o \033[32m{:.2f}\033[m'.format(v1, v2))
elif v2 > v1: 
    print('O \033[32m{:.2f}\033[m é maior do que o \033[32m{:.2f}\033[m'.format(v2, v1))
else: 
    print('\033[32m{:.2f}\033[m e \033[32m{:.2f}\033[m são iguais'.format(v1, v2))
