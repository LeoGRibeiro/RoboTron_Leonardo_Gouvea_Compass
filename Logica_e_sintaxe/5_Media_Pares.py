result = 0
freq_par = 0

for i in range(20):
    while True:
        value = input(f'Insira o {i+1}º valor: ')

        try:
            value = int(value)  # Permitir somente numeros inteiros

        except:
            print('Insira somente números inteiros!')

        else:
            if value % 2 == 0:  # Para considerar apenas os valores pares
                result += value
                freq_par += 1
            break

print(f'A média dos números pares resultou em: {result/freq_par:.1f}')
