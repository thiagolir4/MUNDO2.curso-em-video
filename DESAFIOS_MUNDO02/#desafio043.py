print('='*50)
alt = float(input('Digite aqui quanto você tem de altura: '))
p = float(input('Digite aqui qual é o seu peso: '))
imc = (p / ((alt * alt)*100))*100
print ('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.50:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.50 and imc < 25.00:
    print('Você está no PESO IDEAL')
elif imc >= 25.00 and imc < 30.00:
    print('Você está no SOBREPESO')
elif imc >= 30.00 and imc < 40.00:
    print('Você está com OBESIDADE')
else: 
    print('Você está com OBESIDADE MORBITA')
print('='*50)