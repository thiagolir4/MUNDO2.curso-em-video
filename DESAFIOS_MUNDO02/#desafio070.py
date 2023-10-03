preçoa = 0
total = 0
produtob = menor = c = 0
barato = ' '
while True: 
    produto = str(input('NOME DO PRODUTO: '))
    preço = float(input('Qual o preço R$'))
    c += 1 
    cont = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
    total += preço 
    if preço >= 1000: 
        preçoa += 1 
    if c == 1 or preço < menor: 
        menor = preço
        barato = produto
    if cont == 'N':
        break
print(f'O preço total foi de {total:.2f}')
print(f'Total de produtos mais caros do que R$1000,00: {preçoa:.2f}')
print(f'O produto mais barato é o {barato} e custou  {menor:.2f}')
