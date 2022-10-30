print('________________PESO IDEAL 2___________________')

# Valores
sexo = input('Informe o seu sexo: (masculino, feminino) ')
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

r = float(peso / altura ** 2)

# Condição
if sexo == 'masculino':
    if r < 19:
        print('Abaixo do Peso')
    elif r < 24 and r >= 19:
        print('Peso ideal')
    elif r >= 24: 
        print('Acima do Peso')

elif sexo == 'feminino':
    if r < 20:
        print('Abaixo do Peso')
    elif r < 25 and r >= 20:
        print('Peso ideal')
    elif r >= 25: 
        print('Acima do Peso')
else:
    print('Sexo Inválido?')
