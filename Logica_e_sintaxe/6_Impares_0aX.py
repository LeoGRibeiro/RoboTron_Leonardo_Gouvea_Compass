num = 1

while True:
    limit = input('Insíra um valor maior que 2: ')

    try:
        limit = int(limit)
    except:
        print('Você deve inserir um número inteiro!')
    else:
        if limit > 2:
            break
        else:
            print('Você deve inserir um número maior que 2!')

print(f'Número ímpares entre 0 e {limit}:')
for c in range(limit):
    if c % 2 != 0:  # Para printar somente número impares
        print(c, end=', ')
