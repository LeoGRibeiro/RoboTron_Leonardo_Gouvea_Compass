import pandas as pd

# Para importar somente algumas colunas:
# arquivo = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',', usecols=['Nome','Sobrenome'})

# Para delimitar o número de linhas:
# arquivo = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',', nrows=10)

# Para printar somente os 5 primeiros
# print(venc_oscar.head())

# para importar o arquivo inteiro(sep=',' serve para delimitar as divisões
venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',')

print(venc_oscar)
