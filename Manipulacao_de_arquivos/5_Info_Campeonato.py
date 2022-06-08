import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Campeonato.json', encoding='UTF-8') as json2:
        json_lido = json.load(json2)
        return json_lido


campeonato = obter_json()

print('Chaves: Valores')
# Para melhor leitura
for chaves in campeonato:  # Para percorrer todas as chaves
    print('-', chaves, end=': ')  # Para printar as chaves
    print(campeonato[f'{chaves}'])

print()
# Formato bruto
print(campeonato)

print()
# Outra alternativa, como na primeira questão'
with open('Partida.json', 'r', encoding='UTF-8') as partida:

    json_orig = partida.read()

    print(json_orig)
