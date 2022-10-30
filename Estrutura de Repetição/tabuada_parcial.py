print('________________TABUADA PARCIAL DE UM NÚMERO POSITIVO___________________')

# Condicão de parada 1
loop = True

# Lista de Valores
valores = []

# Lista de Fatorandos
fatorandos = []

# Condição de parada 2
entradas = 0


while loop:
    valor = int(input('Digite um número positivo: '))

    # Condição de parada 
    intervalo = int(input('Digite o intervalo: '))

    if valor > 0:

        # Resultado anterior
        resultado_anterior = 0
        
        while entradas <= intervalo:
            resultado = valor * entradas

            if intervalo > resultado:
                valores.append(resultado)
            else:
                # Condição para que o resultado anterior não se altere
                if resultado_anterior == 0:
                    resultado_anterior = resultado

                # Garante que não irá passar o valor (A)
                valores.append(resultado_anterior - valor)
            
            fatorandos.append(entradas)
            entradas += 1
            
        
        valores.sort(reverse=True)
        fatorandos.sort(reverse=True)

        chave = 0
        for item in valores:
            print(f'{valor} x {fatorandos[chave]} = {item}')

            chave += 1
            
        loop = False

            
            

