print('________________PESO IDEAL V1___________________')
 
# Altura e Peso
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

r = float(peso / altura ** 2)

if r < 20:
    print('Abaixo do Peso')
elif r < 25 and r >= 20 :
    print('Peso ideal')
elif r >= 25: 
    print('Acima do Peso')
