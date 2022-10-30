print('________________PRODUTO DA MATRIZ 1___________________')

# Vetor
vetores = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

# Índices
i = 0

while i < len(vetores):
    vetores[i] = int(input(f'Digite o {i + 1}° valor: '))
    i += 1

# Constante para multiplicar
const = int(input('Digite um valor para multiplicar o vetor: '))

i = 0

while i < len(vetores):
    # Multiplicação
    res = const * vetores[i]
    vetores[i] = res

    i += 1
