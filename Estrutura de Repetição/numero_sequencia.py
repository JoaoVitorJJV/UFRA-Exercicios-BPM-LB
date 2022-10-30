print('________________N NÚMEROS DA SEQUÊNCIA 1___________________')

# Condição de parada 1
loop = True

# Números ímpares
impares = 1

while loop:
    # Final da Sequência
    
    final_sequencia = int(input('Digite a quantidade de valores que você deseja ver: ( < 100) '))
    
    if final_sequencia < 100 and final_sequencia > 0:
        # Valores
        ultimo_valor = 1

        # Condição de parada 2
        entrada = 1

        # Soma dos valores
        soma_valores = 0

        while entrada <= final_sequencia:

            #Fórmula sequência
            valor_sequencia = ultimo_valor + impares
            ultimo_valor = valor_sequencia

            soma_valores += valor_sequencia

            # Transforma e mantém a variável impares com números ímpares
            impares += 2
            entrada += 1
    
        print(f'A soma dos primeiros {final_sequencia} valores dessa sequência é de: {soma_valores}')
        loop = False
    else:
        print('O valor digitado precisa ser menor que 100! \n')
        
        

