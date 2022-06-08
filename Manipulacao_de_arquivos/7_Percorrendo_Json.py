import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Campeonato.json', encoding='UTF-8') as json2:
        json_lido = json.load(json2)
        return json_lido


campeonato = obter_json()

print('Principais chaves: ')
for chaves in campeonato:  # Para percorrer todas as chaves
    print('->', chaves, end=' \n')  # Para printar as chaves
