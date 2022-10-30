print('________________LISTANDO MULHERES___________________')

# Valor máximo
valor_maximo = 20

# Condição de parada 1
loop = True

while loop:
    # Condição de parada 2
    i = 0

    # Dicionário 
    dicionario_dados = {
        'masculino': {},
        'feminino': {}
    }

    while i < valor_maximo:
        # Dados
        sexo = input(f'Sexo da {i + 1}° pessoa: (F, M) ')

        if sexo == "F" or sexo == "M":
         
            idade = int(input(f'Idade da {i + 1}° pessoa: '))

            if idade > 0:
                nome = input(f'Nome da {i + 1}° pessoa: ')
                if sexo == "F":
                    dicionario_dados['feminino'][f'Pessoa{i}'] = {
                        'Nome': nome,
                        'Sexo': sexo,
                        'Idade': idade
                    }
                else:
                    dicionario_dados['masculino'][f'Pessoa{i}'] = {
                        'Nome': nome,
                        'Sexo': sexo,
                        'Idade': idade
                    }

                i +=1
            else:
                print('Só aceitamos valores positivos de idade! \n')
        else:
            print('Só aceitamos os valores M e F no sexo! \n')
    
    for i in dicionario_dados['feminino']:
        print('Nome: ')
        print(dicionario_dados['feminino'][i]['Nome'])
        print('Idade: ')
        print(dicionario_dados['feminino'][i]['Idade'])
        print('Sexo: ')
        print(dicionario_dados['feminino'][i]['Sexo'])
        print('\n')


    loop = False
        






