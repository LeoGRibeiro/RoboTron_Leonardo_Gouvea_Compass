import pandas as pd

# Lendo apenas a coluna 'Age' usando o parametro 'usecols=[]'
venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',', usecols=['Age'])

print(venc_oscar)
