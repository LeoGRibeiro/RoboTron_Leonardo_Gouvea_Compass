import pandas as pd

tabela = pd.read_csv('Elementos.txt', encoding='UTF=8', sep=',')
lista_simb = tabela['Simbolo'].tolist()  # Para conferir de forma mais facil


def mostrar_propriedade(prop): # Função para printar apenas uma propriedade
    print(tabela[[f'{prop}']])


# Menu de opções
while True:
    option = input('Bem vindo! O que deseja fazer?\n1 <- Listar somente propriedades\n2 <- Mostrar propriedades de '
                   'um elemento\n3 <- Listar todos elementos e propriedades\n4 <- Sair\n==> ')

    # Outro menu para escolha de propriedade
    if option == '1':
        while True:
            perg_prop = input('Qual propriedade dos elementos você deseja ver?\n1 <- Simbolo\n2 <- Nome\n3 <- '
                              'Número Atômico\n4 <- Estado Físico a 0 ºC\n5 <- Voltar\n==> ')
            if perg_prop == '1':
                mostrar_propriedade('Simbolo')
            elif perg_prop == '2':
                mostrar_propriedade('Nome')
            elif perg_prop == '3':
                mostrar_propriedade('NumeroAtomico')
            elif perg_prop == '4':
                mostrar_propriedade('EstadoFisico')
            elif perg_prop == '5':
                break
            else:
                print('Insira um número de 1 a 4!')

    # Inserção de simbolos
    elif option == '2':
        while True:
            perg_elem = input('Insira o simbolo do elemento desejado para mostrar '
                              'todas suas propriedades(Insira 99 para sair):\n==> ')
            if perg_elem in lista_simb:
                print(tabela[tabela['Simbolo'] == f'{perg_elem}'])
            elif perg_elem == '99':
                break
            else:
                print('Este elemento não se encontra em nossa tabela')
    # Printar a tabela completa
    elif option == '3':
        print(tabela)
    # Sair do programa
    elif option == '4':
        exit()
