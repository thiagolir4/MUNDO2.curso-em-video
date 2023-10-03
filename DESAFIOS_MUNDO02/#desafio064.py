n = 0
num = 0
soma = 0
fim = 999
while num < fim:
    num = int(input('Digite um numero até [999] '))
    n += 1
    soma += num
    if num >= fim:
        soma -= num
        n -= 1
print('Somando todos os {} numero digitados, o resultado é de {}'.format(n , soma))