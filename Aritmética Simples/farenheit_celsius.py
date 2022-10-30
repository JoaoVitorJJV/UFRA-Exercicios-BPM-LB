from math import floor

print('________________CELSIUS PARA FAHRENHEIT___________________')

#Temperatura em Célsius
temperatura_c = float(input('Digite a temperatura em graus Celsius: '))

#conversao
conversao = (temperatura_c * 1.8) + 32

print('{:.0f}°C \n'.format(temperatura_c))
print(f'{conversao}°F')