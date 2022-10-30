print('________________SOMA DE 1 A 100___________________')

# Valor máximo 
valor_maximo = 100

# Condição de parada
entrada = 1

while entrada < valor_maximo:

    # Soma, o +1 garante que o antecessor irá somar com seu sucessor
    resultado = entrada + entrada + 1
    print(f'{entrada} + {entrada + 1} = {resultado}')

    entrada += 1