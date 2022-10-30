print('________________SEGUNDO MAIOR QUE PRIMEIRO___________________')

# Valores
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

# Verificar se o primeiro já é maior que o segundo

if y > x:
    input('Programa finalizado!')
else:
    # Condição de parada
    loop = True

    while loop:
        novo_valor = int(input('Digite o segundo valor novamente: '))
        y = novo_valor
        
        if y > x:
            loop = False
            input('Programa finalizado!')
            
    