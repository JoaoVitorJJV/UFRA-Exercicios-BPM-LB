print('________________TESTE DO RETÂNGULO___________________')

# Valores
a = int(input('Digite o primeiro cateto: '))
b = int(input('Digite o segundo cateto: '))
c = int(input('Digite o valor da hipotenusa: '))

# Cálculo
soma_cateto = a ** 2 + b ** 2
hipotenusa = c ** 2

if soma_cateto == hipotenusa:
    print('O Triângulo é Retângulo')
else:
    print('Não é um triângulo retângulo')