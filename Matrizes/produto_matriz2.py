print('________________PRODUTO DA MATRIZ 2___________________')

# Vetores
vetor1 = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

vetor2 = vetor1

# Índices
i = 0

while i < len(vetor1):
    vetor1[i] = int(input(f'Digite o {i + 1}° valor: '))
    i += 1

# Constante para multiplicar
const = int(input('Digite um valor para multiplicar o vetor: '))

i = 0

while i < len(vetor2):
    # Multiplicação
    res = const * vetor2[i]
    vetor2[i] = res

    i += 1

print(vetor2)