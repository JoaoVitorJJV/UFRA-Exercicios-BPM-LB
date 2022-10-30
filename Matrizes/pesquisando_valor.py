print('________________PESQUISANDO VALOR___________________')

# Máximo de valors
maximo = 20

# Vetor
vetor = []

# Condição de parada 1
i = 0

# Condição de parada 2
loop = True

while loop:

    qtd_valores = int(input('Quantos valores você deseja armazenar? (max 20) '))

    if qtd_valores <= maximo:
        while i < qtd_valores:
            valor = int(input(f'Digite o {i + 1}° valor: '))
            
            vetor.append(valor)
            i += 1

        # Condição de parada 3
        loop2 = True

        while loop2:
            # Pega o valor que deseja ser procurado
            valor_digitado = int(input('Digite o valor a ser procurado: '))

            # Verifica se o valor existe no vetor
            if valor_digitado in vetor:

            # Pega o índice no vetor, utilizando a função nativa index
                pos = vetor.index(valor_digitado)

                print(f'O valor digitado está na posição: {pos}')
            else:
                print('O valor não existe no vetor. \n')

            # Resposta se deseja continuar
            continuar = input('Deseja fazer uma nova consulta? (s, n) ')

            if continuar == 's' or continuar == 'n' or continuar == 'S' or continuar == 'N':
                if continuar == 'n' or continuar == 'N':
                    loop = False
                    loop2 = False
                
            else:
                print('Comando incorreto, só aceitamos os valores s ou n \n')

    else:
        print(f'A quantidade de itens não pode ser maior que {maximo}!')

