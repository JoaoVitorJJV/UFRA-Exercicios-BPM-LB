from math import ceil, pi

# Forma Geométrica
print('________________CALCULAR ÁREAS___________________')
forma = input(
    'Digite a forma geométrica para calcular a área (quadrado, retangulo, triangulo, circulo): ')

if forma == 'quadrado':
    tipo_de_area_q = input(
        'Como você deseja cácular a área? (lados, diagonal): ')
    if tipo_de_area_q == 'lados':
        # Lados
        lado1 = int(input('Digite o primeiro lado do Quadrado: '))
        lado2 = int(input('Digite o segundo lado do Quadrado: '))

        # Cálculo da área
        area_qua = lado1 * lado2

        print(f'A Àrea do Qudrado informado foi de: {area_qua}')
    elif tipo_de_area_q == 'diagonal':
        diagonal1 = int(input('Digite a primeira diagonal: '))
        diagonal2 = int(input('Digite a segunda diagonal: '))

        area_quadrado2 = ceil((diagonal1 * diagonal2) / 2)

        print(f'A Àrea do Quadrado informado foi de: {area_quadrado2}')

elif forma == 'retangulo': 
    #Base
    base_ret = int(input('Digite a altura do Retângulo: '))

    #Altura
    altura_ret = int(input('Agora digite a altura do Retângulo: '))

    #Calculo da área
    area_ret = base_ret * altura_ret

    print(f'A Àrea do Retângulo informado foi: {area_ret}')

elif forma == 'triangulo':
    #Base
    base_tri = int(input('Digite a base do triângulo: '))

    #Altura
    altura_tri = int(input('Digite a altura do triângulo: '))

    #Calculo da Àrea
    area_tri = base_tri * altura_tri

    print(f'A Àrea do Triângulo foi de: {area_tri}')

elif forma == 'circulo':
    #Diâmetro
    diametro_circulo = float(input('Digite o diâmetro do círculo: '))
    raio = diametro_circulo / 2

    #Cálculo da Àrea
    area_circulo = pi * raio ** 2

    print('A Àrea do círculo informado é de: {:.2f}'.format(area_circulo))


else:
    print('Ops! Comando incorreto, tente novamente')
