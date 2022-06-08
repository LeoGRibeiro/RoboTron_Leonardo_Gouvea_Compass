import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Partida.json', encoding='UTF-8') as partida:
        json_lido = json.load(partida)
        return json_lido


copa_do_brasil = obter_json()
dados_partida = copa_do_brasil['copa-do-brasil'][0]  # Para facilitar a varredura do arquivo

print('Informações do time visitante: ')
for c in dados_partida['time_visitante']:      # Para listar as chaves no time visitante
    print('-', c, end=': ')                    # Para mostrar os nomes das chaves
    print(dados_partida['time_visitante'][c])  # Para mostrar os valores das chaves

print('\nPara comparação: ')
print(dados_partida['time_visitante'])