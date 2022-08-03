'''
Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam
alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador.
O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador
ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"

Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em
Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais
de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está
definido abaixo para que a correção automática do trabalho funcione corretamente.

O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima
jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.

Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido.
Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do
computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora,
como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e
quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a
retirar em cada jogada.

Cuidado: o corretor automático não funciona bem se você tiver alguma chamada a input() antes da definição de todas as funções do jogo (a menos que essa
chamada esteja dentro de uma função). Se seu programa usar input() sem que ele esteja dentro de alguma função, coloque-o no final do programa.

Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja
funcionando, você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar
o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma

Placar: Você ??? X ??? Computador

'''



# n = número de peças inicial
# m = número máximo de peças a ser retiradas por jogador

# a estratégia do computador para ganhar consiste em deixar sempre um número de peças 
# que seja múltiplo de (m+1) ao jogador. 

def calcula_jogada(n, m):
    
    peças_a_retirar = 0
    
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0: # caso que dá pra retirar peças!
            peças_a_retirar = i
    return peças_a_retirar 
    
def computador_escolhe_jogada(n, m):
    
    if n < m: # caso que peças disponíveis é menor que o número máximo de peças que se pode tirar
        print("O computador tirou %d peças." % n)
        print("Agora restam %d peças no tabuleiro.\n" % (n - n))
        proxima_jogada = n
    
    elif calcula_jogada(n, m) != 0: # caso que o cpu calcula a qtd de peças para retirar
        proxima_jogada = calcula_jogada(n, m)
        print("O computador tirou %d peças." % proxima_jogada)
        print("Agora restam %d peças no tabuleiro.\n" % (n - proxima_jogada))
    
    else: # caso que o cpu retira o maior número de peças possíveis
        print("O computador tirou %d peças." % m)
        print("Agora restam %d peças no tabuleiro.\n" % (n - m))
        proxima_jogada = m

    return proxima_jogada

def usuario_escolhe_jogada(n, m):
    
    jogada_usuario = int(input("Informe sua jogada: "))
                         
    while jogada_usuario <= 0 or jogada_usuario > n or jogada_usuario > m:
        print("Valor incorreto. O valor deve estar entre 1 e %d, ou ser menor que a quantidade de peças disponíveis (%d)"% (n, m))
        jogada_usuario = int(input("Informe sua jogada: "))
    
    print("\nVocê tirou %d peças." % jogada_usuario)
    print("Agora resta %d peças no tabuleiro.\n" % (n - jogada_usuario))
    return jogada_usuario


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    vencedor = 2 # variável de controle para quem venceu. 1 para cpu, 0 para usuário.
    
    peças_restantes = n
    
    if n % (m + 1) == 0: # caso que o computador deixa o usuário começar
        print("Você começa!\n")
        proxima_jogada = 0
        
        while peças_restantes > 0:
            # jogada usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break
            # jogada computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break
                
    else:  # caso que o computador começa a partida
        print("Computador começa!\n")
        while peças_restantes > 0:

            # jogada computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break

            # jogada usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break
    
    if vencedor == 1:
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    elif vencedor == 0:
        print("Fim de jogo! Você ganhou!\n")
        return 0

def campeonato():
    
    rodada = 1
    
    partidas_ganhas_cpu = 0
    partidas_ganhas_usuario = 0
    
    while rodada <= 3:
        print("**** Rodada %d ****" % rodada)
        vencedor = partida()
        if vencedor == 1:
            partidas_ganhas_cpu += 1
        elif vencedor == 0:
            partidas_ganhas_usuario += 1
        rodada += 1
    
    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d x %d Computador" % (partidas_ganhas_usuario, partidas_ganhas_cpu))

def main():
    
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()

main()
