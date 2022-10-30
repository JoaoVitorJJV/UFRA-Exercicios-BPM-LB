from math import pi, floor
print('________________VOLUME DO CUBO E DA ESFERA___________________')

#Valores
r = float(input('Digite o raio da esfera: '))
a = float(input('Digite o valor da aresta: '))

#Volume Esfera
raio_esfera_cubo = r ** 3

volume_esfera = floor(4/3 * pi * raio_esfera_cubo)
volume_cubo = a ** 3

#Volume Livre
volume_livre = volume_esfera + volume_cubo

print('O Volume livre desse ambiente é de: {:.2f}'.format(volume_livre))