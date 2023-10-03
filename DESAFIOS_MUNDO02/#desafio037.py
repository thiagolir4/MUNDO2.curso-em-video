num = int(input('Digite um numero inteiro: '))
print('''escolha uma opção
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1: 
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
else:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))