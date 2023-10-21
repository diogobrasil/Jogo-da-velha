import os
import random

JogarNovamente="s"
Jogadas=0
QuemJoga=2 #O usuário é o jogador 2
MaxJogadas=9
Vit="n"
Velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]   
]

def Tela():
    global Velha
    global Jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + Velha[0][0] + " | " + Velha[0][1] + " | " + Velha[0][2])
    print("   -----------")
    print("1:  " + Velha[1][0] + " | " + Velha[1][1] + " | " + Velha[1][2])
    print("   -----------")
    print("2:  " + Velha[2][0] + " | " + Velha[2][1] + " | " + Velha[2][2])
    print("Jogadas: " + str(Jogadas) )

def JogadorJoga():
    global Jogadas
    global QuemJoga
    global MaxJogadas
    if QuemJoga == 2 and Jogadas < MaxJogadas:
        try:
            L = int(input("Linha: "))
            C = int(input("Coluna: "))
            while Velha[L][C] != " ":
                print("Linha e coluna já estão preenchidas. Digite, novamente, a linha e a coluna.")
                L = int(input("Linha: "))
                C = int(input("Coluna: "))
            Velha[L][C] = "X"
            QuemJoga=1
            Jogadas+=1
        except:
            print("Jogada inválida!")
            os.system("pause")
def cpuJoga():
    global Jogadas
    global QuemJoga
    global MaxJogadas
    if QuemJoga == 1 and Jogadas < MaxJogadas:
        L = random.randrange(0,3)
        C = random.randrange(0,3)
        while Velha[L][C] != " ":
            L = random.randrange(0,3)
            C = random.randrange(0,3)
        Velha[L][C] = "O"
        Jogadas+=1
        QuemJoga=2


def VerificarVitoria():
    global Velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #Vrerifiar linhas
        il=ic=0
        while il < 3:
            soma=0
            ic=0
            while ic < 3:
                if(Velha[il][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria = s
                break
            il+=1
        if(vitoria!="n"):
            break
        #Verificar colunas
        il=ic=0
        while ic < 3:
            soma=0
            il=0
            while il < 3:
                if(Velha[il][ic]==s):
                    soma+=1
                il+=1
            if(soma==3):
                vitoria = s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #verificar diagonal 1
        soma=0
        idiag=0
        while idiag < 3:
            if(Velha[idiag][idiag]==s):
                soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
        #Verificar diagonal 2
        soma=0
        idiagl=0
        idiagc=2
        while idiagc >= 0:
            if(Velha[idiagl][idiagc]==s):
                soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def Redefinir():
    global Velha
    global Jogadas
    global MaxJogadas
    global QuemJoga
    global Vit
    Jogadas=0
    QuemJoga=2 #O usuário é o jogador 2
    MaxJogadas=9
    Vit="n"
    Velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]   
    ]



while(JogarNovamente=="s" or JogarNovamente=="S"):  
    while True:
        Tela()
        JogadorJoga()
        cpuJoga()
        Tela()
        Vit=VerificarVitoria()
        if(Vit!="n")or(Jogadas>=MaxJogadas):
            break
    
    print("FIM DE JOGO" )
    if(Vit=="X" or Vit=="O"):
        print("Resultado: Jogador " + Vit + " venceu!")
    else:
        print("Resultado: Empate!")
    JogarNovamente=input("Jogar novamente?[s/n] ")
    Redefinir()
 