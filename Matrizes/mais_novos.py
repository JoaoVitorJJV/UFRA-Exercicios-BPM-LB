print('________________MAIS NOVOS PRIMEIRO___________________')

# Valor máximo
valor_maximo = 2

# Condição de parada 1
loop = True

while loop:
    # Condição de parada 2
    i = 0

    # Vetor de dados 
    vetor_dados = []

    while i < valor_maximo:
        # Dados
        sexo = input(f'Sexo da {i + 1}° pessoa: (F, M) ')

        if sexo == "F" or sexo == "M":
            idade = int(input(f'Idade da {i + 1}° pessoa: '))

            if idade > 0:
                nome = input(f'Nome da {i + 1}° pessoa: ')

                tupla = (nome, sexo, idade)
                vetor_dados.append(tupla)
               
                i +=1
            else:
                print('Só aceitamos valores positivos de idade! \n')
        else:
            print('Só aceitamos os valores M e F no sexo! \n')
    

    # Organiza e ordena as tuplas em ordem descrecente
    novo_vetor = sorted(vetor_dados, key=lambda pessoa: pessoa[2])

    print(novo_vetor)

    loop = False
        






