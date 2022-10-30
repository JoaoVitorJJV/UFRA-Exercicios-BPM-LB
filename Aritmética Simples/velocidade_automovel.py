print('________________VELOCIDADE DO AUTOMÓVEL___________________')

#Dados
v_ini = int(input('Digite a velocidade inicial (M/s): '))
aceleracao = int(input('Digite a aceleração: (M/s²): '))
tempo_percuso = int(input('Digite o tempo do percurso (segundos): '))

#Conversao para Km/h
v_ini_convertido = float(v_ini * 3.6)
aceleracao_convertido = float(aceleracao * 3.6)
tempo_percuso_convertido = float(tempo_percuso / 60)

#Velocidade Cálculo
v = v_ini_convertido + aceleracao_convertido * tempo_percuso_convertido

print('A Velocidade final desse veículo é de: {:.2f} km/h'.format(v))