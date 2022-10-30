from math import pi

print('________________CALCULAR VOLUME CONE___________________')

#Altura
altura = float(input('Digite a altura do Cone: '))

#Raio da base
raio_base = float(input('Digite o raio da base do Cone: '))
raio_base_quadrado = raio_base ** 2


#Cálculo Àrea
v = (pi * raio_base_quadrado * altura) / 3

print('O Volume do cone informado é de aproximadamente: {:.2f}'.format(v))
