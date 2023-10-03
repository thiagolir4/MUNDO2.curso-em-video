print('VAMOS CALCULAR UMA PROGESSÃO ARITIMETICA')
p = int(input('Qual o primeiro termo?: '))
r = int(input('Qual é a razão?: '))
c = 0
while c < 10:
    print('{}'.format(p), end = ' - ')
#    print('{}'.format(p + r), end = ' - ')
    p += r
    c += 1
print('FIM')