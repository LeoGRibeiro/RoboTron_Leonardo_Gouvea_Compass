import pandas as pd

venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',')

# Usar o "!=" para printar todos os valores difentes do referido
print(venc_oscar[venc_oscar['Movie'] != 'The Revenant'])
