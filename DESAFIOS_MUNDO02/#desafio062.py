print('VAMOS CALCULAR UMA PROGESSÃO ARITIMETICA')
p = int(input('Qual o primeiro termo?: '))
r = int(input('Qual é a razão?: '))
termo = p
cont = 1 
total = 0 
mais = 10
while mais != 0: 
    total = total + mais
    while cont <= total: 
        print('{} - '.format(termo), end ='')
        termo += r
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão finalizada com {} termos'.format(total))