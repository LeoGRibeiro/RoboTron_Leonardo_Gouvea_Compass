import pandas as pd

venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',')

print('Vencedores dos oscar de 1991 e 2016: ')

# Uso do '|' pois queremos mais de um resultado
print(venc_oscar[(venc_oscar['Year'] == 1991) | (venc_oscar['Year'] == 2016)]['Name'])
