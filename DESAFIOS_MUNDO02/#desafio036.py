bv = float(input('Bem vindo! Qual o valor da casa que você quer financiar? '))
sal = float(input('Qual valor do seu salário? '))
anos = float(input('Em quantos anos você vai pagar a casa? '))
parcela = bv / (anos*12) 
permicao = sal / 100 * 30 

if parcela <= permicao:
    print('Seu financimento foi aprovado!!! Você vai pagar de parcela \033[32mR${:.2f}\033[m'.format(parcela))
elif parcela > permicao:
    print('Infelizmente seu financiamento foi negado!! o valor da sua parcela fica maior do que 30% do seu salário, tente novamente com prazo maior')