from math import radians, sin, cos, tan
print('________________FUNÇÕES TRIGONOMÉTRICAS___________________')

#Ângulo
angulo = float(input('Digite o Ângulo: '))

#Cálculos
angulo_teste = radians(angulo)
cosseno = cos(angulo_teste)
seno = sin(angulo_teste)
secante = (1/cosseno)
tg = tan(angulo_teste)

print('cos: {:.2f} \n'.format(cosseno))
print('seno: {:.2f} \n'.format(seno))
print('tg: {:.2f} \n'.format(tg))
print('sec: {:.2f} \n'.format(secante))
