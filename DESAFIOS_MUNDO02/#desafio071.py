nota = nota50 = nota20 = nota10 = nota1 = total =0
while True: 
    saque = int(input('Digite aqui o valor do saque: '))
    total= saque 
    nota50 = saque // 50
    total = total - (nota50 * 50) 
    nota20 = total // 20
    total = total - (nota20 * 20)
    nota10 = total // 10
    total = total - (nota10 * 10)
    nota1 = total // 1
    total = total - (nota1 *1)
    if total == 0: 
        break
print('PROCESSANDO SEU SAQUE >>>>>> ')
print('=== Notas do saque === ')
print(f'{nota50} de R$50.00 \n {nota20} de R$20.00 \n {nota10} de R$10.00 \n {nota1} de R$1.00')