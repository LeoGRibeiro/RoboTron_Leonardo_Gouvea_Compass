
lista_compra = ['Maça', 'Banana', 'Pera']

'''Para facilitar o entendimento, assumi o execício como uma lista de produtos
a serem comprados no supermercado'''

in_lista = []  # Produtos do carrinho que estão na lista de compras
not_lista = []  # Produtos do carrinho que não estão na lista de compras

for i in range(3):
    fruta = str(input(f'Insira o nome da {i+1}º fruta: ')).title()  # Para toda toda palavra começar com letra maiúscula

    if fruta in lista_compra:
        in_lista.append(fruta)  # Inserir na lista de frutas que estão na lista de compras
    else:
        not_lista.append(fruta)  # Inserir na lista de frutas que não estão na lista de compras

print('\nLista de compras: ')
for q in lista_compra:  # Printar a lista de compras
    print('-', q)

print('---------------CARIINHO---------------')
if sorted(in_lista) == sorted(lista_compra):  # Conferir se o carrinho está igual a lista de compras
    print('Você comprou tudo o que precisava!')

else:
    for i in in_lista:  # Printar somente as frutas que estão no carrinho e na lista de compras
        print(i, end=', ')
    print('já está(ão) no carrinho!')

    print('Você esqueceu de colocar', end=' ')
    for q in lista_compra:  # Printar somente as frutas que NÃO estão no carrinho mas estão na lista de compras
        if q not in in_lista:
            print(q, end=', ')
    print('no carrinho!')

    for c in not_lista:  # Printar somente as frutas que estão no carrinho mas NÃO estão na lista de compras
        print(c, end=', ')
    print('não estava(am) na lista de compras.')


