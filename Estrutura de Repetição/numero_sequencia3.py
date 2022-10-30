print('________________N NÚMEROS DA SEQUÊNCIA 3___________________')

# Condição de parada 1
loop = True

# Números ímpares
impares = 1

# Potencias
potencias = 1

while loop:

    # Final sequência
    final_sequencia = int(input('Digite a quantidade de valores que você deseja ver: ( < 50) '))

    if final_sequencia < 50:
        # Condição de parada 2
        entrada = 1

        # Soma Valores
        soma_valores = 0

        # Ultimo divisor da divisão
        ultimo_divisor = 1

        # Ultimo denominador da divisão
        ultimo_denominador = 1
        

        while entrada <= final_sequencia:

            # Incremento da potência (denominador divisão)
            potencias = entrada ** 3

            if entrada == 1:
                divisao = 2
                ultimo_divisor = divisao
                soma_valores += divisao
            else:
                # Soma último número impar + ultimo divisor
                soma_dividor = impares + ultimo_divisor

                divisao = soma_dividor / potencias
                ultimo_divisor = soma_dividor
                soma_valores += divisao
                
            impares += 2
            entrada += 1
            
        
        print('A soma dos primeiros {:.0f} valores dessa sequência é de aproximadamente: {:.1f}'.format(final_sequencia, soma_valores))
        loop = False
    else:
        print('O valor precisa ser menor que 50! \n')

       
