print('________________MAIOR E MENOR VALOR___________________')

#tipo
tipo = input('O que você deseja comparar? (menor valor, maior valor): ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if x == y:
    print('Os valores são iguais.')
    exit()

if tipo == 'maior valor':
    if x > y:
        print(f'O maior valor é: {x}')
    else:
        print(f'O maior valor é: {y}')

elif tipo == 'menor valor':
    if x < y:   
        print(f'O menor valor é: {x}')
    else:
        print(f'O menor valor é: {y}')
else: 
    print('Comando inválido')