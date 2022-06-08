import pandas as pd

# Para transformar uma coluna em outra classe, usa-se o "converters={'Year': str}" como parâmetro
# Referência: https://www.quora.com/How-do-I-convert-strings-in-CSV-into-integer-in-Python
# Na resposta do 'Ardit Sulce'
venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',', converters={'Year': str})

# Para criar uma nova coluna apenas durante a execução
venc_oscar["MovieYear"] = venc_oscar["Movie"] + " " + venc_oscar["Year"]

print(venc_oscar['MovieYear'])
