sexo =  str(input('Digite aqui seu sexo [M/F]  ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor informe seu sexo[M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))