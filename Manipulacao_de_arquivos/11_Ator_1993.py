import pandas as pd
from time import sleep

venc_oscar = pd.read_csv('Oscar.txt', encoding='UTF=8', sep=',')

print('Quem ganhou o oscar em 1993? ')
sleep(1)
print(venc_oscar[venc_oscar['Year'] == 1993]['Name'])
