print('________________TERRENO GRANDE E PEQUENO___________________')

#Valores
base = int(input('Valor da Base: '))
altura = int(input('Valor da altura: '))

#Àrea
area = base * altura

if area > 100:
    print('Terreno Grande')
else:
    print(f'Terreno pequeno! -> A Àrea do Retângulo é de: {area}')