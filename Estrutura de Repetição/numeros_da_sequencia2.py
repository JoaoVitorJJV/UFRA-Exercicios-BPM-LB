print('________________N NÚMEROS DA SEQUÊNCIA 2___________________')

# Condição de parada 1
loop = True

while loop:

    # Final sequência
    final_sequencia = int(input('Digite a quantidade de valores que você deseja ver: ( < 50) '))

    if final_sequencia < 50:
        # Condição de parada 2
        entrada = 1

        # Soma Valores
        soma_valores = 0

        while entrada <= final_sequencia:
            divisao = entrada / (entrada + 1)

            soma_valores += divisao
            entrada += 1
        
        print('A soma dos primeiros {:.0f} valores dessa sequência é de: {:.1f}'.format(final_sequencia, soma_valores))
        loop = False
    else:
        print('O valor precisa ser menor que 50! \n')

       
