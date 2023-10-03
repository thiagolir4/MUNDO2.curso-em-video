from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pes in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(pes)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior +=1
    else: 
        totalmenor += 1
print('Ao todo tivemos {} pessoas MAIORES DE IDADE e {} MENORES DE IDADE'.format(totalmaior, totalmenor))