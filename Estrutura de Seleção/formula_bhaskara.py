from math import sqrt
print('________________FÓRMULA DE BHÁSKARA___________________')

# Valores
ax2 = int(input('ax2: '))
bx = int(input('bx: '))
c = int(input('c: '))

# Delta
delta = bx * bx - (4 * ax2 * c)

if delta > 0:
    x1 = (-bx + sqrt(delta)) / 2 * ax2
    x2 = (-bx - sqrt(delta)) / 2 * ax2

    if x1 == x2:
        print('Duas raízes iguais: x1 = {:.0f}, x2 = {:.0f}'.format(x1, x2))
    elif x1 != x2:
        print('Duas raízes: x1 = {:.0f} x2 = {:.0f}'.format(x1, x2))
else:
    print('Delta negativo')