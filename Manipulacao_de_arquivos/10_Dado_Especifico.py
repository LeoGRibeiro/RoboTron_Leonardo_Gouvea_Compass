import pandas as pd

venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',', converters={'Year': str, 'Age': str})

# Transfomação das informações em lista para melhor conferir se axiste o dado desejado
lista_ano = venc_oscar['Year'].tolist()
lista_idade = venc_oscar['Age'].tolist()
lista_ator = venc_oscar['Name'].tolist()
lista_filme = venc_oscar['Movie'].tolist()


print('Este é o banco de dados sobre os vencedores do Oscar de melhor ator de 1928 a 2016')

# Para procurar qualquer dado no arquivo
while True:
    dado = input('Insira algum dado como, nome ou idade dos atores, nome de filmes em inglês ou ano do oscar, que '
                 'iremos mostrar todas as informações correspondentes! \n=> ')

    # Caso o dado não corresponda a uma lista, ela passará para a próxima
    if dado in lista_ano:
        print(venc_oscar[venc_oscar['Year'] == f'{dado}'])

    elif dado in lista_idade:
        print(venc_oscar[venc_oscar['Age'] == f'{dado}'])

    elif dado in lista_ator:
        print(venc_oscar[venc_oscar['Name'] == f'{dado}'])

    elif dado in lista_filme:
        print(venc_oscar[venc_oscar['Movie'] == f'{dado}'])

    else:
        print('Não encontramos nenhuma informação relacionada a esse dado')


# Pergunta para o usuário se deseja fazer outra pesquisa
    while True:
        cont = input('Deseja fazer outra pesquisa? \n1 <- Sim\n2 <- Não\n==> ')
        if cont == '2':
            print('Obrigado por usar nosso serviço!')
            exit()
        elif cont == '1':
            break
        else:
            print('Insira um número válido')
