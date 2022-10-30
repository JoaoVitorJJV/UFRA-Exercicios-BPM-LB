print('________________VELOCIDADE PERMITIDA___________________')

#Dados
v_ini = int(input('Digite a velocidade inicial (M/s): '))
aceleracao = int(input('Digite a aceleração: (M/s²): '))
tempo_percuso = int(input('Digite o tempo do percurso (segundos): '))

# Conversão
v_ini_convertido = float(v_ini * 3.6)
aceleracao_convertido = float(aceleracao * 3.6)
tempo_percuso_convertido = float(tempo_percuso / 60)

v = v_ini_convertido + aceleracao_convertido * tempo_percuso_convertido

if v < 40:
    print('Veículo muito lento')
elif v <= 60 and v < 40:
    print('Velocidade permitida')
elif v <= 80 and v < 60:
    print('Velocidade de cruzeiro')
elif v <= 120 and v < 80:
    print('Veículo rápido')
elif v > 120:
    print('Veículo muito rápido')