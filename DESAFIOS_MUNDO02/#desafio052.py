numero = int(input('Digite um número: '))
total = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m0 O número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele É PRIMO')
else: 
    print('E por isso ele NÃO É PRIMO')
