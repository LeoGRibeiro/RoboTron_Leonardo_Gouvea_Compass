import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Partida.json', encoding='UTF-8') as partida:
        json_lido = json.load(partida)
        return json_lido


copa_do_brasil = obter_json()
dados_partida = copa_do_brasil['copa-do-brasil'][0]  # Para facilitar a varredura do arquivo

# Associação a variáveis
nomeEstadio = dados_partida['estadio']['nome_popular']
placar = dados_partida['placar']
status = dados_partida['status']

print(f'Nome do estádio: {nomeEstadio}')
print(f'Placar do jogo: {placar}')
print(f'Status da partida: {status}')


