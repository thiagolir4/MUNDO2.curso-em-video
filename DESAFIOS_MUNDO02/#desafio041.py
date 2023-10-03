print('='*50)
print('Vamos vem em qual categoria você se inquadra conforme sua idade: ')
idade = int(input('Em que ano você nasceu: '))
ano = 2023 - idade 
if ano <= 9:
    print('Você é da categoria \033[1;32mMIRIN\033[m')
elif ano > 9 and ano <= 14:
    print('Você é da categoria \033[1;32mINFANTIL\033[m')
elif ano > 14 and ano <= 19:
    print('Você é da categoria \033[1;32mJUNIOR\033[m')
elif ano > 19 and ano <= 20:
    print('Você é da categoria \033[1;32mSÊNIOR\033[m')
else: 
    print('Você é da categoria \033[1;32mMASTER\033[m')