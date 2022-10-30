print('________________COTAÇÃO DÓLAR___________________')

cotacao_dolar = 5.34

#Dólares
dolares = int(input('Digite a quantidade em Dólares: '))

#Cálculo
em_reais = float(cotacao_dolar * dolares)

print(f'{dolares} USD \n')
print(f'R$ {em_reais}')


