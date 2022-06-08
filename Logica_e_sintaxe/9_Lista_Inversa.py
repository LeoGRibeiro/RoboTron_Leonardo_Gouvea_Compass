lista = []
lista_rever = []
for c in range(15):
    num = input(f'Insira o {c+1}º valor: ')  # Por não especificar, considerei qualquer valor possível
    lista.append(num)  # Inserir o valor na lista
    lista_rever.append(num)

lista_rever.reverse() # Para inverter a lista

print('Lista na ordem de inserção: ')  # Para comparação
for c in lista:
    print(c, end=' -> ')
print('Fim')

print('\nLista em ordem inversa: ')
for i in lista_rever:
    print(i, end=' -> ')
print('Fim')
