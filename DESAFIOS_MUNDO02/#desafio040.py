print('='*50)
print('Vamos calcular sua média')
m1 = float(input('Qual foi sua nota do primeiro bimestre:  '))
m2 = float(input('Qual foi sua nota do segundo bimestre: '))
m = (m1 + m2) / 2
print('Sua média foi \033[32m{:.2f}\033[m'.format(m))
if m >= 7.0:
    print('\033[1;32mAPROVADO\033[m')
elif m < 5.0:
    print('\033[1;32mREPROVADO\033[m')
else:
    print('\033[1;32mRECUPERAÇÃO\033[m')

print('='*50) 