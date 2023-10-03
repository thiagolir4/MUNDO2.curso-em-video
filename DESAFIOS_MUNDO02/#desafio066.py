n = c = soma = 0
while True: 
    n = int(input('Digite aqui um numero até [999]: '))
    if n == 999:
        break
    if n > 999:
        print('Número invalido, tente novamente!!!')
        soma -= n
        c -= 1
    soma += n  
    c += 1 
print(f'A soma dos {c} numeros digitados foi de {soma}')
