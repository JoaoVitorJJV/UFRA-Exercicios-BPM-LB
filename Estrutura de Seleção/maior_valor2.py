print('________________MAIOR VALOR 3___________________')

lista = [0, 0, 0]
maior_valor = 0

#Valores
lista[0] = int(input('Primeiro Valor: '))
lista[1] = int(input('Segundo Valor: '))
lista[2] = int(input('Terceiro Valor: '))

for i in lista:
    if i > maior_valor:
        maior_valor = i

print(f'O maior valor digitado é: {maior_valor}')

