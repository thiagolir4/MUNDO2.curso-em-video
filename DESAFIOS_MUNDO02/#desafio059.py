import time
print('=-'*25)
n1 = int(input('Digite o primeiro numero: '))
print('=-'*25)
n2 = int(input('Digite o segundo numero: '))
print('=-'*25)
opção = 0
while opção != 5:
    time.sleep(0.3)
    print('''O que você deseja fazer
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR 
        [ 4 ] NOVO NUMERO
        [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>> Qual sua opção?: '))
    if opção == 1:
        soma = n1 + n2 
        print('A soma de {} + {} é = {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2 
        print('A multiplicação de {} X {} é = {}'.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif opção == 4: 
        n1 = int(input('Digite seu novo numero: '))
        n2 = int(input('Digite o seu novo numero: '))
    elif opção == 5:
        print('FIM')
    else: 
        print('Opção invalida, tente novamente')
print('O programa está encerrando, um momento')
time.sleep(1)
print('=>'*25)
print('Obrigado por utilizar nosso sitema, até a proxima!!')
print('=>'*25)