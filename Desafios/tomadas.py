print('________________TOMADAS___________________')

# Condição de parada
loop = True

# Vetor com as tomadas
tomadas = []
while loop:
    # Resultado da soma das tomadas das réguas
    soma_total = 0

    # Número máximo de tomadas
    n_max_tomadas = 4

    # Condição de parada 2
    entrada = 0

    while entrada < n_max_tomadas:
        valor = int(input(f'Digite o n° de tomadas da {entrada + 1}° régua (precisa ser positivo e estar entre 1 e 6): '))
        if valor >= 1 and valor <= 6:
            tomadas.append(valor)
            entrada += 1
        else:
            print('O valor precisa ser positivo e estar entre 1 e 6.')
     

    # Primeiro somamos todas as tomadas das réguas
    # como guardamos os valores em uma lista, utilizamos o laço for
    for i in tomadas:
        soma_total += i

    # Para o resultado ser correto, a soma total das tomadas das réguas
    # subtraindo 3 
    res = soma_total - 3

    print(f'Número máximo de nootebok por régua é de: {res}')
    loop = False

    