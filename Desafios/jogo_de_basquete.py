print('________________JOGO DE BASQUETE___________________')

# Primeiro precisamos saber quantos jogos o jogador quer contabilizar
n_de_jogos = int(input('Quantos jogos você deseja contabilizar? '))

# Condição de parada
entrada = 0

# Lista com as pontuações
partidas = []

while entrada < n_de_jogos:
    valor = int(input(f'Digite a pontuaçãso do {entrada + 1}° jogo: '))
    partidas.append(valor)
    entrada += 1

# Contabiliza a quantidade de vezes que bateu o seu recorde
recordes = 0

# Pior pontuação da partida, precisamos começar sempre com o primeiro
# valor da lista de partidas
pior_pontuacao = 0

# Última pontuação registrada no laço, para comparamos 
ultimo_valor_maior = 0
ultima_pontuacao_menor = partidas[0]

# Laço que irá verificar a lista
for i in partidas:

    # Excluímos a primeira partida já que não serve
    # como comparação de menor

    if partidas.index(i) > 0:
        if i > ultimo_valor_maior:
            recordes += 1
            ultimo_valor_maior = i
    

    if i < ultima_pontuacao_menor:
        # Verifica a posição no vetor, que significa as partidas. Depois
        # verifica quaç foi a pior pontuação, somamos +1 pois os índices começam com pelo 0
        pior_pontuacao = (partidas.index(i)) + 1
        ultima_pontuacao_menor = i
    
print(f'Pior partida: partida de N° {pior_pontuacao}\nVocê bateu seu recorde {recordes} vezes')
