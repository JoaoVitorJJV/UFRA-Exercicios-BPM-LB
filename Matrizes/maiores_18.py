print('________________MAIORES DE 18 1___________________')

# Valor máximo
valor_maximo = 20

# Condição de parada 1
loop = True

while loop:
    # Condição de parada 2
    i = 0

    # Dicionário 
    dicionario_dados = {
        'maiores_idade': {},
        'menores_idade': {}
    }

    # Quantidade a ser incrementada (pessoas listadas)
    pessoas_listadas = 0

    while i < valor_maximo:
        # Dados
        sexo = input(f'Sexo da {i + 1}° pessoa: (F, M) ')

        if sexo == "F" or sexo == "M":
            idade = int(input(f'Idade da {i + 1}° pessoa: '))

            if idade > 0:
                nome = input(f'Nome da {i + 1}° pessoa: ')

                if idade > 18:
                    pessoas_listadas += 1
                    dicionario_dados['maiores_idade'][f'Pessoa{i}'] = {
                        'Nome': nome,
                        'Sexo': sexo,
                        'Idade': idade
                    }
                else:
                    dicionario_dados['menores_idade'][f'Pessoa{i}'] = {
                        'Nome': nome,
                        'Sexo': sexo,
                        'Idade': idade
                    }

                i +=1
            else:
                print('Só aceitamos valores positivos de idade! \n')
        else:
            print('Só aceitamos os valores M e F no sexo! \n')
    
    for i in dicionario_dados['maiores_idade']:
        print('Nome: ')
        print(dicionario_dados['maiores_idade'][i]['Nome'])
        print('Idade: ')
        print(dicionario_dados['maiores_idade'][i]['Idade'])
        print('Sexo: ')
        print(dicionario_dados['maiores_idade'][i]['Sexo'])
        print('\n')
    
    print(f'Pessoas com mais de 18 anos: {pessoas_listadas}')


    loop = False
        






