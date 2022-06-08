import pandas as pd

venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',')

# Atentar ao uso de 2 colchetes, caso não use, resultará em erro
print(venc_oscar[(venc_oscar['Year'] >= 1987) & (venc_oscar['Year'] <= 1999)][['Name', 'Age']])
