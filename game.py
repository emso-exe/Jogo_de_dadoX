# -*- coding: utf-8 -*-

import random
from os.path import isfile
from math import ceil


def numero_e_tipo_validos():
    numero_tipo_validos = ['par', 'impar', 1, 2, 3, 4, 5, 6]
    numero_tipo = input(
        "1º Escolha seu número da sorte que pode ser de 1 á 6\nou se vai ser 'par' ou 'impar': ")
    if numero_tipo.isdigit() == True:
        numero_tipo = int(numero_tipo)
    else:
        numero_tipo = numero_tipo.lower()
    for i in range(len(numero_tipo_validos)):
        if numero_tipo_validos[i] == numero_tipo:
            return numero_tipo
            break
    else:
        print("\nInformação inválida!\nDigite 'par', 'impar' ou um número de 1 á 6!\n")
        return False


def numero_de_jogadas():
    numero_jogadas = [1, 3, 5, 7]
    try:
        qtde_jogadas = int(
            input("\n2º Digite o número de jogadas (1, 3, 5 ou 7): "))
    except:
        print("\nDigite somente números!\nEscolha 1, 3, 5 ou 7 jogadas!\n")
        return False

    for i in range(len(numero_jogadas)):
        if numero_jogadas[i] == qtde_jogadas:
            return qtde_jogadas
            break
    else:
        print("\nQuantidade inválida!\nEscolha 1, 3, 5 ou 7 jogadas!\n")
        return False


def joga_dado_n_vezes(param):
    if param == False:
        return False
    else:
        lado_sorteado = []
        for i in range(int(param)):
            lado_sorteado.append(random.randint(1, 6))
        return lado_sorteado


def soma_pontos(param1, param2):
    pontos = 0
    if param1 == "par":
        for i in range(len(param2)):
            if param2[i] % 2 == 0:
                pontos += 1
    elif param1 == "impar":
        for i in range(len(param2)):
            if param2[i] % 2 == 1:
                pontos += 1
    elif param1 == 1:
        for i in range(len(param2)):
            if param2[i] == 1:
                pontos += 3
    elif param1 == 2:
        for i in range(len(param2)):
            if param2[i] == 2:
                pontos += 3
    elif param1 == 3:
        for i in range(len(param2)):
            if param2[i] == 3:
                pontos += 3
    elif param1 == 4:
        for i in range(len(param2)):
            if param2[i] == 4:
                pontos += 3
    elif param1 == 5:
        for i in range(len(param2)):
            if param2[i] == 5:
                pontos += 3
    else:
        for i in range(len(param2)):
            if param2[i] == 6:
                pontos += 3
    return pontos


def vitoria_ou_derrota(pontos, numero_jogadas, numero_tipo):
    if numero_tipo == 'par' or numero_tipo == 'impar':
        pontos_corte = ceil(int(len(numero_jogadas))/2) * 1
    else:
        pontos_corte = ceil(int(len(numero_jogadas))/2) * 3

    print("\n - Números sorteados: ", numero_jogadas)
    print(" - Número de jogadas: ", int(len(numero_jogadas)))
    print(" - Número de pontos:  ", pontos)
    print(" - Número apostado:   ", numero_tipo)

    if pontos >= pontos_corte:
        print("\n 💚 Você VENCEU! 😍 💚\n")
        resultado = "vitoria"
    else:
        print("\n 💔 Você PERDEU! 😭 💔\n")
        resultado = "derrota"

    dados = (numero_jogadas, int(len(numero_jogadas)),
             pontos, numero_tipo, resultado)
    return dados


def gravar_dados(t):
    dados = ('{};{};{};{};{}'.format(t[0], t[1], t[2], t[3], t[4]))

    if not isfile('jogo_de_dadox.csv'):
        cabecalho = ('nsort;njog;nponto;vapost;stat')
        try:
            with open("jogo_de_dadox.csv", "a") as arquivo:
                arquivo.write(cabecalho)
                arquivo.write('\n')
                arquivo.write(dados)
                arquivo.write('\n')
        except Exception as e:
            print(e, ": Ocorreu um erro na criação do arquivo!")
    else:
        try:
            with open("jogo_de_dadox.csv", "a") as arquivo:
                arquivo.write(dados)
                arquivo.write('\n')
        except Exception as e:
            print(e, ": Ocorreu um erro na gravação dos dados!")


if __name__ == '__main__':

    print('''
    +-------------------------------------------------------+
    |                 🎲 JOGO DE DADOX 🎲                   |
    +-------------------------------------------------------+
    |  1º Digite seu número da sorte (1 à 6) ou se prefere  |
    |     apostar em números pares ou ímpares.              |
    +-------------------------------------------------------+
    |  2º Digite a quantidade de jogadas (1, 3, 5 ou 7)     |
    |     que irá apostar.                                  |
    +-------------------------------------------------------+
    |  3º Cruze os dedos e boa sorte!                       |
    +-------------------------------------------------------+
    ''')
    param1 = numero_e_tipo_validos()
    if param1 != False:
        param2 = joga_dado_n_vezes(numero_de_jogadas())
        if param2 != False:
            gravar_dados(vitoria_ou_derrota(
                soma_pontos(param1, param2), param2, param1))
