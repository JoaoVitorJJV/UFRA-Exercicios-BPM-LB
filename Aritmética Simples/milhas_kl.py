
print('________________MILHAS PARA QUILÔMETROS___________________')

#Milhas
milhas = float(input('Digite as milhas: '))

#Valor aproximado de uma milhas em quilometros 
milhas_em_quilometros = 0.621

#Conversão
conversao = milhas * milhas_em_quilometros

print('{:.0f} milhas em quilômetros é aproximadamente: {:.2f}km'.format(milhas, conversao))


