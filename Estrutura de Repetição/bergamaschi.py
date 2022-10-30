print('________________BERGAMASCHI___________________')

# Final da sequencia
sequencia = 20

# Condição de parada
entrada = 0

# Valores
ante_penultimo_valor = 1
penultimo_valor = 1
ultimo_valor = 1

while entrada <= sequencia:
    if entrada < 3:
        print('1')
    else:
        valor_sequencia = ultimo_valor + penultimo_valor + ante_penultimo_valor
        ante_penultimo_valor = penultimo_valor
        penultimo_valor = ultimo_valor
        ultimo_valor = valor_sequencia
        print(f'{valor_sequencia}')

    entrada += 1

