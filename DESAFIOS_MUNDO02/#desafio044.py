p = float(input('Qual o valor da sua compra?R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] = DINHEIRO/CHEQUE
[ 2 ] = CARTÃO
[ 3 ] = 2X NO CARTÃO
[ 4 ] = 3X OU MAIS NO CARTÃO''''')
fm = int(input('Selecione a fomr ade pagamento: '))
if fm == 1:
    total =  (p * 10 /100)
    print('Sua compra foi de R${:.2f} e com o desconto ficou R${:.2f}'.format(p, (p - total)))
elif fm == 2:
    total = (p * 5 /100)
    print('Sua compra foi de R${:.2f} e com o desconto ficou R${:.2f}'.format(p, (p - total)))
elif fm == 3:
    total = p
    parcela = p / 2
    print('Sua compra foi de R${:.2f} e não teve desconto foi divida em 2X e ficou R${:.2f} por parcela'.format(total, parcela))
elif fm == 4: 
    parcelado = int(input('Em quantas parcelas você vai pagar?: '))
    total = ((p * 20 / 100) + p )/ parcelado
    print('Sua compra foi de R${:.2f} e for parcelada em {}X o valor final foi de R${:.2f}'.format(p, parcelado, total))
else: 
    print('OPÇÃO DE PAGAMENTO INVALIDA, SUA COMPRA FOI DE R${:.2f} e vai ficar R${:.2f}'.format(p, p))