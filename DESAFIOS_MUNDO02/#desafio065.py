c= 0
maior = 0 
menor = 0 
continuar = ''
n = 0
num = 0
while continuar != 'N': 
    n = int(input('Digite um numero aqui: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    c += 1
    num += n 
    media = num / c
print('O a so ma dos seus numeros é igual a {} e você digitou {} numeros, a média entre eles é de {}'.format(num, c, media)) 
