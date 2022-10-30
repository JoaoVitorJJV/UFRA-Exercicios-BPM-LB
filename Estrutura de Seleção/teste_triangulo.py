print('________________TESTE DO TRIÂNGULO___________________')

#Lados
a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))

if a + b != c:
    # Isósceles
    if a == b and c != a and c != b:
        print('O Triângulo é Isósceles')
    # Escaleno
    elif a != b and b != c:
        print('O Triângulo é Escaleno')

    # Equilátero
    elif a == b == c:
        print('O Trângulo é Equilátero')
else:
    print('A forma digitada não é um triângulo')
    