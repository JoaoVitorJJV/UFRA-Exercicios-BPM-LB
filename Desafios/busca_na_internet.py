print('________________BUSCA NA INTERNET___________________')

# Quntidade de pessoas que clicam no 3° link
x = int(input('Quantidadede pessoas que clicaram no 3° link: '))

if x >= 1 and x <= 1000:
    # A quantidade de pessoas que clicou no primeiro, é o quádruoplo
    # de pessoas que clicou no terceiro, então multiplicamos por 4
    res = x * 4

    print(f'Quantidade de pessoas que clicou no 1° link é de : {res}')
else:
    print('A quantidade precisa estar entre 1 e 1000!')