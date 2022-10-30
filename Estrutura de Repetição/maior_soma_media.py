import math

print('________________MAIOR, SOMA E MÉDIA___________________')

# Condição de parada 1
loop = True

# Quantidade de valores
qtd_valores = 10

while loop:
    # Condição de parada 2
    entrada = 1

    # Valores
    maior_valor = 0
    soma_valores = 0
    media_aritmetica = 0
    
    while entrada <= qtd_valores:
        valor = int(input(f'Digite o {entrada}° valor: '))
        
        if valor > 0:
            if valor > maior_valor:
                maior_valor = valor
            
            soma_valores += valor
        else:
            continue

        entrada += 1

    calcular_media = math.floor(soma_valores / qtd_valores)
    print(f'O maior valor: {maior_valor} \nA soma dos valores: {soma_valores} \nMédia: {calcular_media}')
    loop = False

    