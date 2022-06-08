import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Campeonato.json', encoding='UTF-8') as json2:
        json_lido = json.load(json2)
        return json_lido


campeonato = obter_json()

print('-Edição atual: ')
for q in campeonato['edicao_atual']:
    print(q, end=': ')
    print(campeonato['edicao_atual'][q])
    break  # Usei o break para printar somente o primeiro valor

print('-Fase atual: ')
for q in campeonato['fase_atual']:
    print(q, end=': ')
    print(campeonato['fase_atual'][q])
    break

print('-Rodada atual: ')
for q in campeonato['rodada_atual']:
    print(q, end=': ')
    print(campeonato['rodada_atual'][q])
    break

print()
################### VERSÃO 2 ######################
print('-Edição atual:')
print(campeonato['edicao_atual']['edicao_id'])

print('-Fase atual:')
print(campeonato['fase_atual']['fase_id'])

print('-Rodada atual:')
print(campeonato['rodada_atual']['nome'])
