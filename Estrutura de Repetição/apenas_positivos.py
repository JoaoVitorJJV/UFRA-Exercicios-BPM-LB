print('________________APENAS POSITIVOS___________________')

# Condição de parada
loop = True

while loop:
    valor = int(input('Digite um número positivo para parar o programa: '))

    if valor > 0 :
        # Termina o loop
        loop = False
