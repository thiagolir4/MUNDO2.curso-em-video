homem = 0
mulher = 0
maioridade = 0
while True: 
    idade = int((input('IDADE: ')))
    sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1 
    if sexo == 'M':
        homem +=1
    if sexo =='F':
        if idade <= 20: 
            mulher += 1
    if cont == 'N':
        break
print (f'Total de pessoa com mais de 18 anos: {maioridade}')
print (f'Total de homens cadastrados: {homem}')
print (f'Total de mulheres com menos de 20 anos: {mulher}')
