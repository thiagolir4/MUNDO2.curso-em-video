t = 0
cont = 0
for n in range (0,6):
    num =int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0:
        t += num
        cont += 1
print('Dos numeros digitados {} foram pares e a soma deles é de {}'.format(cont, t))