print('-'*30)
print('SEQUENCIA DE FIBONCCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?: '))
p = 0
s = 1
print('{}-{}'.format(p,s), end='-')
c = 3
while c <= n:
    soma = p + s
    print('{}'.format(soma), end ='-')
    p = s 
    s = soma
    c += 1  
print('FIM')