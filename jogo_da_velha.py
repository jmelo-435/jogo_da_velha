import os
import random

#mostrar um tabuleiro

#receber a entrada de dados do jogador

#checar se houve vitória ou empate

#mudar de jogador

#checar se houve empate ou vitória denovo

jogadas=0
quem_joga="X"
jogar_contra_maquina=None
vencedor=None
jogo_em_andamento = True
mensagem_de_erro =None


"""
Matriz 3X3 que representa o tabuleiro 
"""
velha=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

"""
Função que exibe o tabuleiro em tela
"""

def exibir_tabuleiro(velha):
    os.system('cls')
    print("Quem joga: " + quem_joga)
    print('   0   1   2')
    print('0 ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('--------------')
    print('1 ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('--------------')
    print('2 ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print("Jogadas: "+str(jogadas))

"""
Função que administra os dados inseridos pelo jogador
"""

def processar_entrada_de_dados_do_jogador(velha):
    global mensagem_de_erro
    global jogadas
    global jogar_contra_maquina
    
    if jogar_contra_maquina==None:
        resposta = input("Deseja jogar contra máquina?(s/n)=>")
        if resposta=="s":
            jogar_contra_maquina=True
        elif resposta=="n":
            jogar_contra_maquina=False
        else:
            print("Insira uma resposta válida(s/n)")
            processar_entrada_de_dados_do_jogador(velha)
    
    if mensagem_de_erro!=None:
        print(mensagem_de_erro)
    dado= input("Insira uma coordenada(Ex: 0,1)=>")
    try:
        coordenada_vertical = int(dado[0])
        coordenada_horizontal = int(dado[-1])
    except:
        mensagem_de_erro=("Os dados inseridos estavam incorretos, ou essa casa já está ocupada!")
        return
    
    if coordenada_horizontal<=2 and coordenada_vertical<=2 and velha[coordenada_vertical][coordenada_horizontal]== " ":
        velha[coordenada_vertical][coordenada_horizontal]= quem_joga
        mensagem_de_erro=None
        jogadas =jogadas+1
    else:
        mensagem_de_erro=("Os dados inseridos estavam incorretos, ou essa casa já está ocupada!")

"""
Funções que checam as condições de vitória ou empate
"""

def checar_vitoria_horizontal(velha):
    global vencedor

    if velha[0][0]==velha[0][1]==velha[0][2] and velha[0][0]!=" ":
        vencedor = velha[0][0]
        return True
    elif velha[1][0]==velha[1][1]==velha[1][2] and velha[1][0]!=" ":
        vencedor = velha[1][0]
        return True
    elif velha[2][0]==velha[2][1]==velha[2][2] and velha[2][0]!=" ":
        vencedor = velha[2][0]
        return True
    
def checar_vitoria_vertical(velha):
    global vencedor

    if velha[0][0]==velha[1][0]==velha[2][0] and velha[0][0]!=" ":
        vencedor = velha[0][0]
        return True
    elif velha[0][1]==velha[1][1]==velha[2][1] and velha[0][1]!=" ":
        vencedor = velha[0][1]
        return True
    elif velha[0][2]==velha[1][2]==velha[2][2] and velha[0][2]!=" ":
        vencedor = velha[0][2]
        return True

def checar_vitoria_diagonal(velha):
    global vencedor

    if velha[0][0]==velha[1][1]==velha[2][2] and velha[0][0]!=" ":
        vencedor = velha[0][0]
        return True
    elif velha[0][2]==velha[1][1]==velha[2][0] and velha[0][2]!=" ":
        vencedor = velha[0][2]
        return True

def checar_empate(velha):
    global vencedor
    global jogo_em_andamento
    if vencedor == None and " " not in velha[0]+velha[1]+velha[2]:
        exibir_tabuleiro(velha)
        print("Deu Velha!")
        jogo_em_andamento=False


"""
Função que une todas as funções de checagem de condições de vitoria ou empate
"""
def checar_condicoes_de_vitoria_e_empate(velha):
    global jogo_em_andamento
    if checar_vitoria_diagonal(velha)or checar_vitoria_horizontal(velha) or checar_vitoria_vertical(velha):
        jogo_em_andamento=False
        os.system('cls')
        exibir_tabuleiro(velha)
        print("O vencedor é: " +vencedor)
    else:
        checar_empate(velha)


"""
Função que alterna a vez entre os jogadores
"""
def mudar_quem_joga():
    global quem_joga
    if quem_joga=="X":
        quem_joga="O"
    else:
        quem_joga="X"
        
"""
Função que dá ao computador a habilidade de fazer movimentos
"""

def maquina(velha,jogar_contra_maquina):
    if not jogar_contra_maquina or not jogo_em_andamento:
        return
    while quem_joga=="O":
        fileira = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if velha[fileira][coluna]== " ":
            velha[fileira][coluna]= "O"
            mudar_quem_joga()
        


"""
Executa as funções lógicas do jogo em loop até que surja um vencedor ou um empate
"""

while jogo_em_andamento:
    exibir_tabuleiro(velha)
    processar_entrada_de_dados_do_jogador(velha)
    checar_condicoes_de_vitoria_e_empate(velha)
    mudar_quem_joga()
    maquina(velha,jogar_contra_maquina)