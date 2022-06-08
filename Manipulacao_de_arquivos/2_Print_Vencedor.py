import json


def obter_json():  # Função vista na masterclass do dia 6
    with open('Partida.json', encoding='UTF-8') as partida:
        json_lido = json.load(partida)
        return json_lido


copa_do_brasil = obter_json()
dados_partida = copa_do_brasil['copa-do-brasil'][0]  # Para facilitar a varredura do arquivo

print(f'Placar do jogo: {dados_partida["placar"]}')
print('Vencedor: ', end='')

# Após analizar o placar do time mandante e visitante, verifica-se quem marcou mais gols e o exiba-o
if dados_partida['placar_mandante'] > dados_partida['placar_visitante']:
    print(dados_partida['time_mandante']['nome_popular'])

elif dados_partida['placar_mandante'] < dados_partida['placar_visitante']:
    print(dados_partida['time_visitante']['nome_popular'])

else:
    print('Empate')
