import random
print('Vamos jogar PEDRA, PAPEL ou TESOURA')
print('''Selecione sua opção
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha = int(input('Sua escolha: '))
p1 = 'PEDRA'
p2 = 'PAPEL'
p3 = 'TESOURA'
lista = [p1, p2, p3]
escolhido = random.choice(lista)
print('O computador escolheu {}'.format(escolhido))
if escolha == 1 and escolhido == p1:
    print('O JOGO EMPATOU')
elif escolha == 1 and escolhido == p2:
    print('VOCÊ PERDEU')
elif escolha == 1 and escolhido == p3:
    print('VOCÊ GANHOU')
elif escolha == 2 and escolhido == p1:
    print('VOCÊ GANHOU')
elif escolha == 2 and escolhido == p2: 
    print('O JOGO EMPATOU')
elif escolha == 2 and escolhido == p3: 
    print('Você perdeu')
elif escolha == 3 and escolhido == p1: 
    print('VOCÊ PERDEU')
elif escolha == 3 and escolhido == p2: 
    print('VOCÊ GANHOU')
elif escolha == 3 and escolhido == p3:
    print('VOCÊ PERDEU')
