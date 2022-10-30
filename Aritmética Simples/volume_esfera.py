from math import pi, floor
print('________________CALCULAR VOLUME ESFERA___________________')
#diametro

diametro = int(input('Digite o diâmetro da esfera: '))

raio = diametro / 2

raio_ao_cubo = raio ** 3

area = floor(float((4/3 * pi * raio_ao_cubo)))

print(f'A Àrea da esfera é aproximadamente: {area}')