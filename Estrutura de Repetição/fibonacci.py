print('________________FIBONACCI___________________')

# Final da sequencia
sequencia = 30

# Condição de parada
entrada = 0

# Valores
penultimo_valor = 1
ultimo_valor = 1

while entrada <= sequencia:
    if entrada < 2:
        print('1')
    else:
        valor_sequencia = ultimo_valor + penultimo_valor
        penultimo_valor = ultimo_valor
        ultimo_valor = valor_sequencia
        print(f'{valor_sequencia}')

    entrada += 1

