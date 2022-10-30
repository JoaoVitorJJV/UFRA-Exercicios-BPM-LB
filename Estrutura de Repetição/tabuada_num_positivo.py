print('________________TABUADA NÚMERO POSITIVO___________________')

# Condição de parada 1
intervalo = 0

# Condição de parada 2
loop = True

while loop:
    # Valor
    valor = int(input('Digite um número positivo: '))
    if valor > 0:

        #Repetição
        while intervalo <= 10:
            resultado = valor * intervalo
            print(f'{valor} x {intervalo} = {resultado}')

            intervalo += 1

        break

