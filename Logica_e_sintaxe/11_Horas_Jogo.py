tempo = 0
while True:
    hora_inic = input('Que horas o jogo começou? ')
    hora_final = input('Que horas o jogo terminou? ')

    try:
        hora_inic = int(hora_inic)  # Para impedir que insiram horários quebradas
        hora_final = int(hora_final)
    except:
        print('Insira horários redondos! Não insira os minutos. ex: 18')

    else:
        if hora_final < 0 or hora_inic < 0 or hora_final > 24 or hora_inic > 24:  # Impedir que insiram horários
            print('Você deve inserir um valor entre 0 e 24 horas!')               # maiores que 24 ou menores que 0
        else:
            break

if hora_final > hora_inic:  # Se o horario final for maior que o inicial, basta subtrair o maior pelo menor
    tempo = hora_final - hora_inic

elif hora_final < hora_inic:  # Se o horario final for maior que o inicial, soma-se 24 ao final e subtraia pelo inicial
    tempo = (hora_final + 24) - hora_inic

elif hora_final == hora_inic:  # Como o minimo é 1 hora e o máximo são 24, quando temos horarios iguais, o resultado
    print('O jogo durou 24 horas')                                                                     # deve ser 24.
    exit()  # Para não printar a linha seguinte
print(f'O jogo durou {tempo} hora(s)')
