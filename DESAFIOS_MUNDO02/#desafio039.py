ano = int(input('Em que ano você nasceu: '))
div = 2023 - ano

if div == 18:
    print('Você está pronto para se alistar, fez 18 anos esse ano')
elif div > 18:
    print('Você já passou do ano para se alistar, você deveria ter se alistado \033[32m{}\033[m anos atrás'.format(div - 18))
else: 
    print('Você ainda não pode se alistar, ainda precisa esperar \033[32m{}\033[m anos'.format(18 - div))
#eu poderia ter usado a tag dat.today().year para o programa sempre se atualizar e utilizar sempre o ano atual para fazer o calculo 