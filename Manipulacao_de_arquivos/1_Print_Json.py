with open('Partida.json', 'r', encoding='UTF-8') as partida:

    resultado = partida.read()  # Usando o "read()" o formato do json é mantido

    print(resultado)
