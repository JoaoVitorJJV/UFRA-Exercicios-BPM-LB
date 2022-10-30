print('________________MAIOR, MENOR, SOMA E MÉDIA, POSITIVOS E NEGATIVOS___________________')

import math

# Condição de parada 1
loop = True

while loop:
    # Condição de parada 2
    entrada = 1

    # Valores
    maior_valor = 0
    soma_valores = 0
    media_aritmetica = 0
    porcentagem_positivos = 0
    porcentagem_negativos = 0

    # Variáveis para saber as porcentagens
    qtd_positivos = 0
    qtd_negativos = 0

    # Quantidade de valores
    qtd_valores = int(input('Com quantos valores você deseja trabalhar? '))

    if qtd_valores > 0 and qtd_valores < 20:
        while entrada <= qtd_valores:
            valor = int(input(f'Digite o {entrada}° valor: '))

            if valor >= 0:
                qtd_positivos += 1
            else:
                qtd_negativos += 1
         
            if valor > maior_valor:
                maior_valor = valor
            
            soma_valores += valor
         
            entrada += 1

        # Calcular porcentagens
        porcentagem_positivos = ((qtd_positivos * qtd_valores) / 100 ) * 100
        porcentagem_negativos = ((qtd_negativos * qtd_valores) / 100 ) * 100

        calcular_media = math.floor(soma_valores / qtd_valores)
        print(f'O maior valor: {maior_valor} \nA soma dos valores: {soma_valores} \nMédia: {calcular_media} \nPorcentagem Valores Negativos: {porcentagem_negativos}% \nPorcentagem Valores Positivos: {porcentagem_positivos}% \n')
        loop = False
    else:
        print('O valor precisa ser positivo e menor que 20! \n')

    

    