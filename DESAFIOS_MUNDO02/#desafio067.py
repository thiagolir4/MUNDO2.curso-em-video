num = 0 
while True:
    num = int(input('Digite um numero para ver a tabuada: '))
    if num < 0:
         break
    for c in range (0,11):
         print(f'{num} x {c:2} = {num*c}')

print('O PROGRAMA TABUADA FOI ENCERRADO!!!')
