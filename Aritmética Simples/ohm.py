from logging.config import valid_ident


print('________________LEI DE OHM___________________')

#Resistência
r = int(input('Digite a resistência do circuito: '))

#Corrente
i = int(input('Digite o valor da corrente elétrica '))

#Lei de Ohm

v = r * i

print(f'A Tensão desse circuito elétrico é de: {v}')