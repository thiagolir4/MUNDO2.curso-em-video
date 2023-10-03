primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -')
print('ACABOU')