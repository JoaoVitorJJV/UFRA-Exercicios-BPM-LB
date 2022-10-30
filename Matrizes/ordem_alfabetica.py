print('________________ORDEM ALFABETICA___________________')

# Limite de pessoas
limite = 20

# Condição de parada
i = 0

# Vetor
vetor = []
while i < limite:
    valor = input(f'Digite o nome da {i + 1}° pessoa: ')
    vetor.append(valor)
    i += 1
vetor.sort()

for i in vetor:
    print(i)
