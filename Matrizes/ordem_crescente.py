print('________________ORDEM CRESCENTE___________________')

# Limite valores
limite = 20

vetor = []

# Condição de parada
i = 0

while i < limite:
    valor = int(input(f'Digite o {i + 1}° valor: '))
    vetor.append(valor)
    i += 1

for i in vetor:
    print(i)