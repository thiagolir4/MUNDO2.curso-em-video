from random import randint
computador = randint(0, 10)
print('Sou seu computador ... acabei de pensar em um numero de 0 a 10')
print('Será que você consegue acertar em qual numero estou pensado?')
print('Vamos tentar!!!')
acertou = False
palpite = 0
while not acertou: 
   jogador = int(input('Qual seu palpite? '))
   palpite += 1
   if jogador == computador:
      acertou = True
   else:
      if jogador > computador:
         print('MENOS... tente mais uma vez')
      elif jogador < computador:
         print('MAIS ... tente mais uma vez')
print('acertou com {} tentativas, PARABENS '.format(palpite))