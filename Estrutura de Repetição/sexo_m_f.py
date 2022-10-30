print('________________SEXO M OU F___________________')

# Valor
sexo = input('Digite o sexo: (S, M) ')

# Condição de parada
loop = True

if sexo == 'M' or sexo == 'F':
    print('Programa Finalizado!')
else:
    while loop:
        novo_valor = input('Digite o sexo: (S, M) ')

        if novo_valor == 'M' or novo_valor == 'F':
            loop = False
    