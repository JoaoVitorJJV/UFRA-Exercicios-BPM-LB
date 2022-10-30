print('________________JOGO DA VELHA___________________')
# Matriz do tabulheiro
tabuleiro = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Função que inicia o jogo (menu inicial)
def inicio():
    # Condição de parada
    loop = True

    while loop:
        iniciar = input('O que você deseja fazer?\nJogar (s)\nSair (n)\n')
        if iniciar == 's':
            main()
            loop = False
        else:
            print('Te vejo na próxima!')
            loop = False


# Função que tem a lógica do jogo
def main():
    global tabuleiro 
    # Controle de jogadas e decide se o jogo vai acabar ou nao
    jogada_atual = 0


    # Chama a função para verificar se há vencedor ou empate
    while verificacao_ganhou() == 0:
        # Iremos utilizar o resto da divisao da variavel jogada_atual
        # para saber a vez do jogador. Essa expressão irá sempre retornar
        # 1 e 2, respectivamente
        print(f'Vez do jogador: {jogada_atual % 2 + 1}')

        # Função que irá inserir as jogadas no tabuleiro
        montar_tabuleiro()

        # Entrada das jogadas
        linha = int(input('\nLinha: '))
        coluna = int(input('Coluna: '))

        # Irá inserir na matriz os dados de acordo com as entradas
        # Como a matriz começa contando do 0, precisamos sempre subtrair
        # 1 de cada jogada
        if tabuleiro[linha - 1][coluna - 1] == 0:
            if (jogada_atual%2+1) ==1:
                tabuleiro[linha-1][coluna-1] = 1
            else:
                tabuleiro[linha-1][coluna-1] = -1
        else:
            print('Essa posição já está ocupada!')
            jogada_atual -= 1


        # Mostra quem ganhou
        if verificacao_ganhou():
            tabuleiro = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
            print(f"O Jogador: {jogada_atual%2+1} ganhou após {jogada_atual + 1} rodadas.")
            inicio()
        elif jogada_atual == 8:
            # Reinicia o tabuleiro
            tabuleiro = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
            print(f'Deu velha!')
            inicio()

        jogada_atual += 1


# Função que sera chamada toda vez na função da lógica do jogo
# ela verifica a coluna com laços de repetição para saber se 
# algum jogador ganhou (retorna 1) ou se deu empate (retorna 0)

def verificacao_ganhou():
    # Laço que irá verificar as linhas da matriz do tabuleiro
    for i in range (3):

        # Essa soma irá definir se algum jogador ganhou, somando
        # cada linhas da matriz
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]

        # Se o resiltado da soma for igual a 3 ou -3, algum jogador ganhou
        if soma == 3 or soma == -3:
            return 1

    # Laço que irá verificar as colunas da matriz, seguindo a mesma
    # lógica do laço acima

    for i in range (3):
        # Os índices são invertidos
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]

        if soma == 3 or soma == -3:
            return 1

    # Precisamos também verificar as diagonais, seguindo a lógica parecia
    # com a acima, porém não precisamos de laços de repetição

    primeira_diagonal = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    segunda_diagonal = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]

    if primeira_diagonal == 3 or primeira_diagonal == -3 or segunda_diagonal == 3 or segunda_diagonal == -3:
        return 1
    
    # Se nenhuma das conções acima for satisfeita, ninguém ganhou, então retornamos 0
    return 0

# Função que irá montar o tabuleiro a cada jogada
def montar_tabuleiro():
    # Laços aninhados que irão colocar as jogadas nas colunas e linhas do tabuleiro
    for i in range(3):
        for a in range(3):
            # Verifica se há espaço na coluna
            if tabuleiro[i][a] == 0:
                print('_', end=' ')
            elif tabuleiro[i][a] == 1:
                print(' X ', end=' ')
            elif tabuleiro[i][a] == -1:
                print(' O ', end=' ')

        # Desenha o tabuleiro
        print()


# Incia o jogo 
inicio()

