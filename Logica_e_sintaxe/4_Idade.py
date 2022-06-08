idade = input('Qual sua idade? ')

try:  # Para permitir somente a entrada de números inteiros
    idade = int(idade)

except:
    print('Insira um número inteiro! ex: 23')

else:
    if idade >= 18:
        print('Você é maior de idade.')
    elif 18 > idade >= 12:
        print('Você é um adolescente.')
    elif 12 > idade >= 0:
        print('Você é uma criança.')
    else:
        print('Você viajou no tempo')
