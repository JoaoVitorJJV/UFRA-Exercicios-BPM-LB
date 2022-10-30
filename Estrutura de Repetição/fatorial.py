print('________________FATORIAL___________________')

# Condição de parada
loop = True

while loop:
    valor = int(input('Digite o valor positivo a ser calculado: '))

   
    if valor > 0:
        # Condição de parada 2
        entrada = 1

        # valores
        ultimo_valor = valor

        total_fatorial = 1
        while entrada <= valor:
            # Cálculo fatorial
            if valor - entrada  > 0:
                calculo = ultimo_valor * (valor - entrada)
                ultimo_valor = calculo
                total_fatorial = calculo

            entrada +=1
        
        print(f'O fatorial do número {valor} é igual a {total_fatorial}')
        # Condição de parada 3
        continuar_execucao = True

        while continuar_execucao:
            continuar = input('Você deseja uma nova execução? (s, n): ')
            if continuar == 'S' or continuar == 's' or continuar == 'n' or continuar == 'N':
                if continuar == 's' or continuar == 'S':
                    continuar_execucao = False

                else:
                    continuar_execucao = False
                    loop = False
            else:
                print('Comando incorreto. tente novamente. \n')
    else:
        print('O Valor precisa ser positivo! \n')

